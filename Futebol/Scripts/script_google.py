"""
Web Scraper FOCADO para Match Logs do FBref usando Selenium
Extrai os logs de partida de uma ÚNICA URL fornecida.
Ideal para testes e extração de temporadas específicas.
"""
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings

warnings.filterwarnings('ignore')

class FBrefSingleLogScraper:
    """
    Scraper focado em extrair o Match Log de uma única URL específica,
    garantindo robustez ao lidar com cookies e carregamento da página.
    """
    
    def __init__(self, headless=True):
        print("🚀 Inicializando navegador automatizado...")
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless=new')
        
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            print("✅ Navegador iniciado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao iniciar o navegador: {e}")
            raise

    def scrape_single_match_log(self, match_log_url: str):
        """
        Extrai a tabela de match logs de uma única página de temporada.
        """
        print(f"\n🔍 Acessando a URL específica: {match_log_url}")
        self.driver.get(match_log_url)

        try:
            # --- ETAPA CRUCIAL PARA ROBUSTEZ ---
            # Espera até 10 segundos para o botão de aceitar cookies e clica nele
            print("⏳ Procurando pelo banner de cookies...")
            wait = WebDriverWait(self.driver, 10)
            accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Accept All"]')))
            accept_button.click()
            print("✅ Banner de cookies aceito.")
            # Pequena pausa para a página se ajustar após o clique
            time.sleep(2)
        except Exception:
            # Se não encontrar o botão, assume que não era necessário
            print("✅ Banner de cookies não encontrado ou já foi aceito anteriormente.")

        print("📊 Extraindo a tabela de logs da página...")
        try:
            # pd.read_html é a forma mais rápida de converter tabelas HTML
            tables = pd.read_html(self.driver.page_source)
            
            # Procura pela tabela correta (a que tem a coluna 'Date')
            matchlog_df = None
            for df in tables:
                if 'Date' in df.columns:
                    # Limpa os cabeçalhos de múltiplos níveis que o read_html pode criar
                    if isinstance(df.columns, pd.MultiIndex):
                        df.columns = df.columns.droplevel(0)
                    matchlog_df = df.copy()
                    break
            
            if matchlog_df is None:
                print("❌ Não foi possível encontrar a tabela de match logs na página.")
                return None
            
            # Limpeza do DataFrame
            matchlog_df = matchlog_df[matchlog_df['Date'] != 'Date'].dropna(how='all').reset_index(drop=True)
            
            # Adiciona colunas de contexto
            season = match_log_url.split('/')[-2]
            player_name = match_log_url.split('/')[-1].split('-Match-Logs')[0].replace('-', ' ')
            matchlog_df['Temporada'] = season
            matchlog_df['Jogador'] = player_name
            
            print(f"✅ Tabela extraída com sucesso! Encontradas {len(matchlog_df)} partidas.")
            return matchlog_df

        except Exception as e:
            print(f"   ❌ Erro ao tentar extrair ou processar a tabela: {e}")
            return None

    def close(self):
        """Fecha o navegador para liberar recursos."""
        if self.driver:
            self.driver.quit()
            print("\n🔒 Navegador fechado com segurança.")

def main():
    """Função principal para executar o scraper."""
    print("="*70)
    print(" SCRAPER DE MATCH LOG - TEMPORADA ÚNICA ".center(70))
    print("="*70)
    
    scraper = None
    try:
        # headless=False para ver o que está acontecendo (bom para debug)
        # mude para True para rodar de forma invisível e mais rápida
        scraper = FBrefSingleLogScraper(headless=True)
        
        # --- URL ALVO ---
        # Coloque aqui o link exato da temporada que você quer extrair
        url_alvo = "https://fbref.com/en/players/d70ce98e/matchlogs/2004-2005/Lionel-Messi-Match-Logs"
        
        # Extrai os dados da URL especificada
        final_df = scraper.scrape_single_match_log(url_alvo)
        
        if final_df is not None and not final_df.empty:
            # Salva o resultado em um arquivo Excel
            season = final_df['Temporada'].iloc[0]
            player_name = final_df['Jogador'].iloc[0].replace(' ', '_')
            filename = f"{player_name}_Match_Logs_{season}.xlsx"
            
            print(f"\n💾 Salvando arquivo...")
            final_df.to_excel(filename, index=False, engine='openpyxl')
            
            print("\n" + "="*70)
            print("🎉 PROCESSO CONCLUÍDO COM SUCESSO! 🎉".center(70))
            print(f"📁 Arquivo salvo como: {filename}")
            print("="*70)
            print("\n📋 PREVIEW DOS DADOS (5 primeiras linhas):")
            # Usar to_string() para garantir que todas as colunas sejam mostradas no preview
            print(final_df.head().to_string())
            
        else:
            print("\n❌ Falha na extração. Nenhum dado foi salvo.")

    except Exception as e:
        print(f"\n❌ Ocorreu um erro fatal no processo: {e}")
    finally:
        if scraper:
            scraper.close()

if __name__ == "__main__":
    main()