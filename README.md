 Last-Mile Delivery Failure Prediction  Group 12 (Logistics)

## Project Overview

This project addresses a real-world problem in the **logistics sector**: predicting whether a delivery will **fail or succeed** before it happens, using operational, environmental, and route-related data from last-mile deliveries in Nigeria.
Delivery failures (missed drop-offs, flooded roads, unavailable customers, vehicle breakdowns, wrong addresses, etc.) cost logistics companies time, fuel, and customer trust. By predicting failure risk in advance, dispatchers and delivery partners can intervene early rerouting, reassigning drivers, confirming addresses, or rescheduling  instead of reacting after the fact.

**Goal:** Build and deploy a machine learning model that predicts `delivery_failure` (0 = Delivered, 1 = Failed) for a given delivery, based on features known at or near dispatch time.

## Problem Statement

Given details about a delivery such as distance, package type, vehicle, weather, traffic, road condition, driver experience, and delivery attempts can we predict whether that delivery will fail?

This is framed as a **binary classification problem**, with `delivery_failure` as the target variable.

## Dataset

**File:** `Delivery_prediction_Dataset_.xlsx`

- **10,000 delivery records**, 30 columns
- Covers deliveries across **6 Nigerian states** (Oyo, FCT, Kano, Lagos, Enugu, Rivers) and **10 cities**
- **4 delivery partners:** Jumia Logistics, Kobo360, GIG Logistics, Kwik
- **Target distribution:** ~41% failed deliveries vs. ~59% delivered (reasonably balanced)

### Key columns

| Column | Description |
|---|---|
| `delivery_id` | Unique identifier for the delivery |
| `delivery_partner` | Logistics company handling the delivery |
| `order_date` / `delivery_date` | Order and delivery dates |
| `state` / `city` | Delivery location |
| `package_type` | Category of package (Electronics, Food, Documents, etc.) |
| `vehicle_type` / `delivery_mode` | How the delivery was made |
| `weather_condition` | Sunny, Harmattan, Heavy Rain, etc. |
| `traffic_level` / `road_condition` | Route conditions |
| `distance_km` / `package_weight_kg` | Physical delivery attributes |
| `expected_time_hours` / `actual_time_hours` | Planned vs. actual delivery duration |
| `driver_id` / `driver_experience` / `driver_rating` | Driver-related features |
| `customer_available` / `address_verified` | Recipient-side risk factors |
| `payment_method` | Cash on Delivery / Transfer |
| `fuel_level` / `vehicle_breakdown` | Vehicle status |
| `delivery_attempts` | Number of attempts made |
| `holiday` | Whether the delivery date was a holiday |
| `delivery_cost_ngn` | Cost of the delivery (NGN) |
| `failure_reason` | Reason for failure (e.g. Flood, Vehicle Breakdown, Customer Not Home, Heavy Traffic, Wrong Address) — only populated when a delivery fails |
| `delivery_status` | "Delivered" or "Failed" |
| `delivery_failure` | **Target variable** — 1 if failed, 0 if delivered |

> Note: `failure_reason` and `delivery_status` are outcomes of the delivery and will be excluded (or handled carefully) as model features to avoid data leakage, since they wouldn't be known before the delivery happens.

## Project Plan

1. **Problem definition & dataset selection** — this document
2. **Exploratory Data Analysis (EDA)** — understand distributions, correlations, and failure patterns across weather, traffic, distance, driver experience, etc.
3. **Data preprocessing** — handle missing values, encode categorical features, address potential data leakage
4. **Model development** — train and compare classification models (e.g. Logistic Regression, Random Forest, XGBoost)
5. **Model evaluation** — accuracy, precision, recall, F1-score, ROC-AUC (with attention to false negatives, since missed failure predictions are costly)
6. **Deployment** — expose the model via a simple web app/API so dispatchers can get a failure-risk prediction for a new delivery before it's dispatched

## Repository Structure

```
├── data/                # Dataset(s)
├── notebooks/           # EDA and experimentation notebooks
├── src/                 # Preprocessing, training, and inference scripts
├── models/              # Saved trained models
├── app/                 # Deployment app/API
└── README.md
```

## Team — Group 12

**archimede** mulundaarchimede@gmail.com
---
---


## Status
**Exploratory Data Analysis (EDA)**
