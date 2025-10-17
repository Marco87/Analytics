# 💼 Consumer Financial Complaints Analytics – Power BI Dashboard  
### Developed for the [**DataDNA Challenge – October 2025 (Onyx Data)**](https://datadna.onyxdata.co.uk/challenges/october-2025-datadna-consumer-financial-complaints-analytics-challenge/?ck_subscriber_id=1387339873&utm_source=convertkit&utm_medium=email&utm_campaign=The%20October%202025%20DataDNA%20Dataset%20Challenge%20has%20Begun!%20-%2019181388)

---

## 📘 Project Overview
This project was created as part of the **DataDNA Challenge (October 2025)**, hosted by **Onyx Data**.  
The goal was to analyze **consumer financial complaints in the United States** and visualize insights using **Power BI** in a clean, modern, and business-oriented dashboard.  

The dashboard provides a comprehensive overview of complaint patterns, company performance, and response efficiency, enabling users to explore and compare key indicators interactively.

---

## 🎯 Objectives
- Evaluate the **efficiency and timeliness** of company responses to consumer complaints.  
- Identify **regional and temporal trends** in customer dissatisfaction.  
- Measure the relationship between **reputation, company size, and market share**.  
- Deliver a **visually engaging and easy-to-use dashboard** for decision-makers and analysts.  

---

## 🧱 Data Model Structure
The data model follows a **Star Schema**, with a fact table containing complaint records and a company dimension providing company-level details.

### **Fact Table – `Complaints`**
Includes all consumer complaint records with attributes such as:
- Complaint ID, submission and receipt dates  
- State, product, sub-product, issue, and sub-issue  
- Channel of submission (Web, Phone, Referral, etc.)  
- Response time (in days) and timeliness flag  
- Company identifier and region/division classifications  

### **Dimension Table – `Company`**
Contains company-level information used for performance benchmarking:
- Market share percentage  
- Reputation score (range 50–100)  
- Company size tier (Small, Medium, Large)  
- Average response time and timely response rate  
- Complaint normalization KPI (Complaints per 1% market share)

---

## 📊 Dashboard Overview
The Power BI dashboard was designed to present both **macro insights** and **company-level performance** through dynamic visuals and clear KPIs.

**Main KPIs:**
- Total number of distinct companies  
- Total complaints  
- Average response time (days)  
- Average reputation score  
- Timely response rate  

**Main Visuals:**
- 📍 **Interactive filters** by company, region, product, sub-product, issue, and sub-issue  
- 📈 **Summary KPIs** displayed in the top banner  
- 🗺️ **Complaints by State** (geographical analysis)  
- 🥧 **Complaints by Company Size and Submission Channel**  
- 📊 **Complaints by Product** (category breakdown)  
- 🕒 **Complaints by Semester** (trend analysis)  
- 📋 **Company performance table** with key indicators  

---

## 🎨 Design and Layout
The dashboard design combines a **modern gradient background** (purple–blue tone) with **white workspace areas**, resulting in a professional and visually appealing layout.

**Design highlights:**
- Sidebar with navigation filters and gradient background  
- Consistent use of color to distinguish categories and KPIs  
- Clean layout with strong visual hierarchy and easy navigation  
- Alignment with **corporate analytics dashboard aesthetics**

**Tools Used:**
- 🧩 Power BI Desktop  
- 🎨 Figma (for background design and layout)  

---

## 💡 Key Insights
- States like **California, Florida, and Texas** register the highest number of complaints.  
- **Large companies** receive the majority of complaints but tend to respond more promptly.  
- The **Web channel** dominates as the main submission method (>70% of total complaints).  
- Most complaints are related to **traditional financial products** such as checking accounts and credit cards.  
- The **average reputation score (≈75)** reflects overall strong performance but with significant company variation.  

---

## 👤 Author
**Marco Alencastro**  
Data Analyst | Power BI Developer  

🔗 [LinkedIn](https://www.linkedin.com/in/marco-alencastro/)  
🌐 [Portfolio](https://allen87.com/)