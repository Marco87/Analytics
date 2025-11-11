"""
Web Scraper DEFINITIVO para FBref usando Selenium
Contorna proteções anti-bot simulando navegador real
Extrai estatísticas completas de jogadores para Power BI
Autor: Assistente Claude
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from datetime import datetime
import re
import warnings
warnings.filterwarnings('ignore')


class FBrefSeleniumScraper:
    """Scraper usando Selenium para contornar proteções anti-bot"""
    
    def __init__(self, headless=True):
        """
        Inicializa o scraper
        headless=True: navegador invisível (mais rápido)
        headless=False: mostra navegador (útil para debug)
        """
        print("🚀 Inicializando navegador automatizado...")
        
        # Configurar opções do Chrome
        chrome_options = Options()
        
        if headless:
            chrome_options.add_argument('--headless=new')
        
        # Opções para parecer mais humano
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        # Remover indicadores de webdriver
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        try:
            # Instalar e iniciar ChromeDriver automaticamente
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Executar script para esconder webdriver
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            print("✅ Navegador iniciado com sucesso!")
            
        except Exception as e:
            print(f"❌ Erro ao iniciar navegador: {e}")
            print("\n🔧 SOLUÇÃO:")
            print("Instale o Chrome se não tiver: https://www.google.com/chrome/")
            raise
    
    def extract_player_info(self, soup):
        """Extrai informações básicas do jogador"""
        info = {
            'Nome': 'N/A',
            'Posicao': 'N/A',
            'Nacionalidade': 'N/A',
            'Data_Nascimento': 'N/A',
            'Altura': 'N/A',
            'Peso': 'N/A',
            'Pe_Preferido': 'N/A'
        }
        
        # Nome
        h1 = soup.find('h1')
        if h1:
            info['Nome'] = h1.text.strip()
        
        # Meta informações
        meta_div = soup.find('div', {'id': 'meta'})
        if meta_div:
            paragraphs = meta_div.find_all('p')
            for p in paragraphs:
                text = p.get_text()
                
                if 'Position:' in text:
                    info['Posicao'] = text.split('Position:')[1].split('▪')[0].strip()
                
                if 'Footed:' in text:
                    footed = re.search(r'Footed:\s*(\w+)', text)
                    if footed:
                        info['Pe_Preferido'] = footed.group(1)
                
                if 'Born:' in text:
                    born_match = re.search(r'Born:\s*(\w+\s+\d+,\s+\d{4})', text)
                    if born_match:
                        info['Data_Nascimento'] = born_match.group(1)
                
                if 'cm' in text:
                    height_match = re.search(r'(\d+)cm', text)
                    if height_match:
                        info['Altura'] = height_match.group(1) + ' cm'
                
                if 'kg' in text:
                    weight_match = re.search(r'(\d+)kg', text)
                    if weight_match:
                        info['Peso'] = weight_match.group(1) + ' kg'
            
            # Nacionalidade
            nationality_span = meta_div.find('span', {'class': 'f-i'})
            if nationality_span:
                nat_text = nationality_span.find_next_sibling(text=True)
                if nat_text:
                    info['Nacionalidade'] = nat_text.strip()
        
        return info
    
    def extract_all_stats_tables(self, html_content):
        """Extrai todas as tabelas de estatísticas"""
        all_dataframes = {}
        
        try:
            # Parsear HTML
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Encontrar todas as tabelas de estatísticas
            stat_tables = soup.find_all('table', {'class': 'stats_table'})
            
            print(f"📊 Encontradas {len(stat_tables)} tabelas de estatísticas")
            
            for idx, table in enumerate(stat_tables):
                try:
                    # ID da tabela
                    table_id = table.get('id', f'table_{idx}')
                    
                    # Caption/título
                    caption = table.find('caption')
                    table_name = caption.text.strip() if caption else table_id
                    
                    # Limpar nome
                    table_name = re.sub(r'[^\w\s-]', '', table_name)
                    table_name = table_name.replace(' ', '_')[:31]
                    
                    # Converter para DataFrame
                    df = pd.read_html(str(table))[0]
                    
                    # Limpar colunas multi-nível
                    if isinstance(df.columns, pd.MultiIndex):
                        df.columns = ['_'.join(map(str, col)).strip('_') for col in df.columns.values]
                    
                    # Limpar nomes
                    df.columns = [str(col).strip() for col in df.columns]
                    
                    # Remover linhas vazias
                    df = df.dropna(how='all')
                    
                    if not df.empty:
                        all_dataframes[table_name] = df
                        print(f"   ✓ {table_name}: {len(df)} registros")
                    
                except Exception as e:
                    print(f"   ⚠ Erro na tabela {idx}: {e}")
                    continue
            
            return all_dataframes
            
        except Exception as e:
            print(f"❌ Erro ao extrair tabelas: {e}")
            return {}
    
    def scrape_player(self, player_url):
        """Extrai dados completos de um jogador"""
        print(f"\n{'='*70}")
        print(f"🔍 Acessando página do jogador...")
        print(f"🌐 URL: {player_url}")
        print(f"{'='*70}\n")
        
        try:
            # Navegar para a página
            self.driver.get(player_url)
            
            # Aguardar carregamento (comportamento humano)
            print("⏳ Aguardando carregamento da página...")
            time.sleep(5)
            
            # Rolar a página (simular comportamento humano)
            print("📜 Rolando a página...")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            time.sleep(2)
            
            # Pegar HTML completo
            html_content = self.driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Extrair informações
            print("📋 Extraindo informações básicas...")
            player_info = self.extract_player_info(soup)
            
            print(f"✅ Jogador: {player_info['Nome']}")
            print(f"✅ Posição: {player_info['Posicao']}")
            print(f"✅ Nacionalidade: {player_info['Nacionalidade']}")
            
            # Extrair tabelas
            print("\n📊 Extraindo tabelas de estatísticas...")
            all_tables = self.extract_all_stats_tables(html_content)
            
            print(f"\n✅ Total de tabelas extraídas: {len(all_tables)}")
            
            return {
                'info': player_info,
                'tables': all_tables,
                'url': player_url
            }
            
        except Exception as e:
            print(f"❌ Erro ao processar jogador: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def close(self):
        """Fecha o navegador"""
        try:
            self.driver.quit()
            print("\n🔒 Navegador fechado")
        except:
            pass
    
    def save_to_excel(self, player_data, filename=None):
        """Salva dados em Excel com múltiplas abas"""
        if not player_data:
            print("❌ Nenhum dado para salvar")
            return None
        
        if filename is None:
            player_name = player_data['info']['Nome'].replace(' ', '_')
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'{player_name}_stats_{timestamp}.xlsx'
        
        print(f"\n{'='*70}")
        print(f"💾 Salvando dados em Excel...")
        print(f"{'='*70}\n")
        
        try:
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                # Aba de informações básicas
                df_info = pd.DataFrame([player_data['info']])
                df_info.to_excel(writer, sheet_name='Info_Basicas', index=False)
                print(f"✅ Aba: Info_Basicas")
                
                # Abas de estatísticas
                for table_name, df in player_data['tables'].items():
                    sheet_name = table_name[:31]
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                    print(f"✅ Aba: {sheet_name} ({len(df)} linhas)")
            
            print(f"\n{'='*70}")
            print(f"🎉 ARQUIVO SALVO COM SUCESSO!")
            print(f"📁 {filename}")
            print(f"📊 Total de abas: {len(player_data['tables']) + 1}")
            print(f"{'='*70}\n")
            
            return filename
            
        except Exception as e:
            print(f"❌ Erro ao salvar: {e}")
            return None
    
    def create_unified_dataframe(self, player_data):
        """Cria dataframe unificado com estatísticas principais"""
        if not player_data or not player_data['tables']:
            return pd.DataFrame()
        
        # Procurar tabela principal
        main_table = None
        
        for name, df in player_data['tables'].items():
            if 'standard' in name.lower() or 'stats' in name.lower():
                main_table = df.copy()
                break
        
        if main_table is None and player_data['tables']:
            main_table = list(player_data['tables'].values())[0].copy()
        
        if main_table is not None:
            # Adicionar info do jogador
            for key, value in player_data['info'].items():
                main_table[key] = value
            return main_table
        
        return pd.DataFrame()


def main():
    """Função principal"""
    
    print("""
    ╔═══════════════════════════════════════════════════════════════════╗
    ║        SCRAPER DEFINITIVO - FBref com Selenium                    ║
    ║        Contorna TODOS os bloqueios anti-bot! 🚀                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    scraper = None
    
    try:
        # Perguntar sobre modo visual
        print("\n🎨 Deseja ver o navegador funcionando?")
        print("1 - Não (mais rápido, invisível)")
        print("2 - Sim (útil para debug)")
        
        modo = input("\nEscolha (1 ou 2): ").strip()
        headless = modo != '2'
        
        # Inicializar scraper
        scraper = FBrefSeleniumScraper(headless=headless)
        
        # URL do jogador
        print("\n" + "="*70)
        print("Cole a URL do jogador (ou Enter para Messi):")
        player_url = input("🔗 URL: ").strip()
        
        if not player_url:
            player_url = "https://fbref.com/en/players/d70ce98e/Lionel-Messi"
            print(f"📌 Usando: {player_url}")
        
        if 'fbref.com/en/players/' not in player_url:
            print("❌ URL inválida!")
            return
        
        # Extrair dados
        player_data = scraper.scrape_player(player_url)
        
        if player_data:
            # Salvar Excel
            filename = scraper.save_to_excel(player_data)
            
            if filename:
                # Criar unificado
                print("\n💡 Criando arquivo unificado...")
                df_unified = scraper.create_unified_dataframe(player_data)
                
                if not df_unified.empty:
                    unified_file = filename.replace('.xlsx', '_unificado.xlsx')
                    df_unified.to_excel(unified_file, index=False)
                    print(f"✅ Arquivo unificado: {unified_file}")
                
                print("\n" + "="*70)
                print("🎯 PRÓXIMOS PASSOS - POWER BI:")
                print("="*70)
                print("1. Abra Power BI Desktop")
                print("2. Obter Dados → Excel")
                print(f"3. Selecione: {filename}")
                print("4. Escolha as abas desejadas")
                print("5. Crie seus dashboards! 📊⚽")
                print("="*70)
                
                # Preview
                if not df_unified.empty:
                    print("\n📋 PREVIEW DOS DADOS (5 primeiras linhas):")
                    print(df_unified.head().to_string())
        else:
            print("\n❌ Não foi possível extrair os dados")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Processo interrompido pelo usuário")
    
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        if scraper:
            scraper.close()


if __name__ == "__main__":
    print("\n📦 INSTALAÇÃO DE DEPENDÊNCIAS:")
    print("Execute uma vez:")
    print("pip install selenium webdriver-manager pandas beautifulsoup4 openpyxl lxml")
    print("\n" + "="*70 + "\n")
    
    main()