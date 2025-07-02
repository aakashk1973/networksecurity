## Network security project for phising data

## About the Dataset

This dataset is designed for a network-security classifier that predicts whether an attack (e.g. phishing/malicious URL) is likely. It contains URL- and domain-level features extracted from web requests, DNS records, and page metadata. Key columns include:

- **having_IP_Address**: URL uses a raw IP instead of domain name  
- **URL_Length**: total length of the URL string  
- **Shortining_Service**: use of a URL shortener service  
- **having_At_Symbol**: presence of `@` in the URL  
- **double_slash_redirecting**: unusual `//` redirects  
- **Prefix_Suffix**: use of hyphens in domain (e.g. `my-site.com`)  
- **having_Sub_Domain**: number of subdomains  
- **SSLfinal_State**: SSL certificate status (valid / expired / self-signed)  
- **Domain_registeration_length**: days since domain registration  
- **Favicon**: whether favicon loaded from same domain  
- **port**: non-standard port usage  
- **HTTPS_token**: presence of “HTTPS” in URL path  
- **Request_URL**: external resource requests ratio  
- **URL_of_Anchor**: ratio of safe vs. suspicious anchor links  
- **Links_in_tags**: proportion of links in `<link>`/`<script>` tags  
- **SFH**: server form handler – external vs. internal  
- **Submitting_to_email**: form action pointing to an email address  
- **Abnormal_URL**: deviations from typical URL structure  
- **Redirect**: count of HTTP redirects  
- **on_mouseover**: use of JavaScript `onmouseover` events  
- **RightClick**: disabling right-click functionality  
- **popUpWidnow**: presence of pop-up windows  
- **Iframe**: usage of `<iframe>` tags  
- **age_of_domain**: domain age in months  
- **DNSRecord**: existence of valid DNS records  
- **web_traffic**: Alexa or similar traffic rank  
- **Page_Rank**: Google PageRank score  
- **Google_Index**: whether URL is indexed by Google  
- **Links_pointing_to_page**: backlink count  
- **Statistical_report**: final aggregated risk score  
- **Result**: class label (benign = 0 / malicious = 1)  

---

## ETL & Model Training Pipeline Architecture

![ETL Pipeline Architecture]

This end-to-end pipeline performs data extraction, validation, transformation, model training/evaluation and deployment:

1. **Data Ingestion**  
   - **Source:** MongoDB  
   - **Component:** `DataIngestionComponent`  
   - **Output Artifacts:** raw data dumps, schema metadata  

2. **Data Validation**  
   - **Component:** `DataValidationComponent`  
   - **Checks:** schema conformity, missing values, data drift  
   - **Output Artifacts:** validation reports, cleaned records  

3. **Data Transformation**  
   - **Component:** `DataTransformationComponent`  
   - **Tasks:** feature engineering, scaling, encoding  
   - **Output Artifacts:** transformed datasets, feature store entries  

4. **Model Training**  
   - **Component:** `ModelTrainerComponent`  
   - **Input:** transformed dataset + training config  
   - **Output Artifacts:** trained model binaries, training logs  

5. **Model Evaluation**  
   - **Component:** `ModelEvaluationComponent`  
   - **Metrics:** accuracy, F1, ROC-AUC (as configured)  
   - **Output Artifacts:** evaluation report  

6. **Model Pushing**  
   - **Component:** `ModelPusherComponent`  
   - **Decision:** if evaluation ≥ threshold → push to staging/production  
   - **Deployment Targets:** AWS / Azure model registry or container endpoint  
   - **Output Artifacts:** deployment manifests, endpoint URLs  

---

### How to use

1. Place your pipeline config files in `config/`  
2. Run `python run_pipeline.py --config config/pipeline.yaml`  
3. Check generated artifacts under `artifacts/` and deployed model in your cloud account  
