# Transformer Research Ideas for EV Charging Load Forecasting

> สรุปไอเดียต่อยอดจาก literature synthesis และผล benchmark ในโฟลเดอร์ Thesis
>
> เป้าหมายหลัก: พัฒนา Transformer สำหรับ EV charging load forecasting ที่คาดการณ์ peak ได้ดีขึ้น ให้ uncertainty ที่เชื่อถือได้ และยังมีประสิทธิภาพเมื่อพยากรณ์หลาย horizon

## สถานะปัจจุบันที่ควรใช้เป็นฐาน

- ใช้กรอบทดลองแบบ Encoder-only + Direct Multi-step Forecasting
- Input window ปัจจุบันประมาณ 96 steps และ output 48 steps หรือ 24 ชั่วโมงที่ความละเอียด 30 นาที
- เปรียบเทียบ Base Transformer, Informer, Autoformer, TFT และ PatchTFT แล้ว
- Autoformer เด่นที่ 30 นาที ส่วน Informer เด่นในช่วง 3–24 ชั่วโมง
- PatchTFT ยังไม่ชนะอย่างสม่ำเสมอ จึงยังไม่ควรสรุปว่า patching เหมาะกับ EV load โดยอัตโนมัติ
- Peak Zone WAPE ยังสูงประมาณ 25–37% สะท้อนปัญหา peak-load underestimation

## กลุ่ม A: ไอเดียที่แนะนำมากที่สุด

### A1. Peak-aware Probabilistic Transformer (รองรับ Gaps P-1 ถึง P-5)

**แนวคิด**

เปลี่ยนจาก point forecast เป็น quantile forecast เช่น P10, P50 และ P90 พร้อมแก้ปัญหา Quantile Crossing (P-1), Autoregressive Accumulation (P-2), Non-stationarity Recalibration (P-3) และเพิ่มน้ำหนักให้ช่วง peak ใน loss

**องค์ประกอบที่เป็นไปได้**

- Transformer, Informer หรือ Mamba backbone
- Multi-quantile output head แบบ Direct Multi-step (DMS)
- Pinball loss + Peak-weighted loss (Peak-Pinball)
- PICNN head หรือ Monotonic Layer เพื่อป้องกัน Quantile Crossing (P-1)
- Adaptive Conformal Prediction (ACI) Recalibration สำหรับ Non-stationary environment (P-3)

**Research question**

> Transformer/Mamba ที่ใช้ peak-aware quantile loss ร่วมกับ PICNN และ Conformal Recalibration สามารถลด peak error และสร้าง prediction interval ที่ calibrated ดีเยี่ยมโดยไม่เกิด Quantile Crossing ได้หรือไม่?

**การประเมิน**

- MAE, RMSE, WAPE (สำหรับ P50 / Median)
- Peak Zone WAPE
- CRPS (Continuous Ranked Probability Score)
- PICP ที่ระดับ 80% และ 90% (วัด Coverage Ratio)
- PINAW (Prediction Interval Normalized Average Width)
- Winkler Score & Quantile Calibration Plot (Reliability Diagram)
- การทดสอบ Quantile Crossing Rate (ต้องเป็น 0%)

**จุดแข็ง**

- แก้ปัญหาตรงจุดกับ Probabilistic Gaps P-1 ถึง P-5 ที่พบใน Literature
- มีประโยชน์ต่อ grid operation, peak shaving และ V2G scheduling
- Contribution ทรงพลัง ครอบคลุมทั้ง Architecture, Loss Function และ Statistical Calibration
- Corpus support ยืนยันแล้ว: PICNN ([[2025_Zheng_Coherent_Hierarchical_EV_Load]]) กับ conformal prediction ([[2024_Zhou_Conformal_Prediction_DER]]) มีใน corpus แล้ว แต่ไม่มี paper ใดผูกกับ Mamba/cross-attention backbone — คอมโบเต็มจึงยัง novel ตาม [[research_gaps]]

**ความเสี่ยง**

- ต้องกำหนด peak threshold และน้ำหนัก loss อย่างมีหลักการ
- PICNN อาจลดความคม (Sharpness) ของ tail quantiles ต้องจูนร่วมกับ Conformal Recalibration

---

### A2. Controlled Multi-scale Transformer Benchmark

**แนวคิด**

ศึกษาอย่างเป็นระบบว่า representation แบบใดเหมาะกับ EV charging load ที่มีทั้งรูปแบบ 30 นาที, รายวัน และรายสัปดาห์

**รูปแบบที่ควรเปรียบเทียบ**

- Point-wise temporal tokens
- Fixed-size patches เช่น 2, 4, 8 และ 12 steps
- Multi-scale patches เช่น 2 + 8 + 48 steps
- Series decomposition: trend + seasonal + residual
- Variate-level tokens แบบ iTransformer
- Hybrid temporal-patch + variate attention

**Research question**

> Tokenization และ temporal inductive bias แบบใดเหมาะที่สุดสำหรับ EV charging load ในแต่ละ forecasting horizon?

**การทดลองที่สำคัญ**

- ใช้ dataset และ split เดียวกันทั้งหมด
- ใช้ prediction head และ training budget เดียวกัน
- รายงานผลแยกตาม horizon 30 นาที, 3, 6 และ 24 ชั่วโมง
- ทำ ablation ของ patch size และ decomposition
- วัด training time และ inference memory ร่วมกับ accuracy

**จุดแข็ง**

- ต่อยอดจากผลที่ PatchTFT แพ้ใน benchmark ได้โดยตรง
- เป็น contribution เชิง methodological ที่ defend ได้ดี
- ไม่จำเป็นต้องสร้างโมเดลที่ซับซ้อนเกินไป

**ความเสี่ยง**

- อาจได้ข้อสรุปเป็น benchmark study มากกว่า novel architecture
- ต้องควบคุม implementation fairness อย่างเข้มงวด

---

### A3. Context-aware Cross-attention Transformer

**แนวคิด**

แยก historical load ออกจาก exogenous variables แล้วใช้ cross-attention เพื่อให้โมเดลเลือกบริบทที่มีผลต่อแต่ละช่วงเวลา แทนการ concatenate ทุก feature เข้าด้วยกัน

**ข้อมูลบริบทที่เป็นไปได้**

- Calendar และ cyclical time encoding
- Weather
- TOU price
- Traffic หรือ station occupancy
- Arrival/departure และ SOC หากมีข้อมูลระดับ session

**Research question**

> Cross-attention สามารถใช้บริบทภายนอกได้มีประสิทธิภาพและตีความได้ดีกว่าการ concatenate features แบบมาตรฐานหรือไม่?

**การประเมิน**

- เปรียบเทียบ concatenation, GRN/VSN และ cross-attention
- วัดผลใน normal period และ peak period แยกกัน
- ใช้ attention analysis หรือ SHAP ตรวจ feature importance
- ทดสอบกรณี missing หรือ noisy covariates

**จุดแข็ง**

- เหมาะกับ Transformer โดยตรง
- สร้าง interpretability contribution ได้
- เชื่อมกับสาเหตุของ peak load ได้ดีกว่าใช้ historical load อย่างเดียว

**ความเสี่ยง**

- ต้องมี exogenous data ที่ timestamp ตรงกันและไม่มี leakage
- Attention weight ไม่ควรถูกตีความเป็น causal effect โดยตรง

## กลุ่ม B: ไอเดียต่อยอดเชิงสถาปัตยกรรม

### B1. RevIN + Decomposition + Transformer

แก้ non-stationarity ของ EV load ด้วย Reversible Instance Normalization ร่วมกับ trend/seasonal decomposition แล้วป้อน residual ให้ Transformer

ควรทดสอบว่าช่วยในช่วงเปลี่ยนฤดูกาล, วันหยุด และ station ที่มี distribution shift หรือไม่

### B2. Dynamic Patch Transformer

ให้โมเดลเลือก patch size หรือ receptive field ตาม volatility ของช่วงเวลา แทนการกำหนด patch size เดียวตลอด sequence

ตัวอย่างคือใช้ patch สั้นในช่วง charging spike และ patch ยาวในช่วงโหลดนิ่ง

### B3. Efficient Long-context Transformer

เปรียบเทียบ standard attention, ProbSparse, linear attention และ local-global attention เมื่อเพิ่ม input window จาก 48 ชั่วโมงเป็น 7–14 วัน

ต้องรายงานทั้ง accuracy, GPU memory, latency และจำนวนพารามิเตอร์ ไม่ใช่เฉพาะ RMSE

### B4. Transformer + Mamba เป็น Ablation/Hybrid

ใช้ Mamba เป็น efficient temporal encoder และ Transformer cross-attention สำหรับ global context หรือ exogenous fusion

ควรเริ่มจากการเป็น baseline/ablation ก่อน ไม่ควรตั้ง novelty จากคำว่า "Mamba + Transformer" เพียงอย่างเดียว เพราะแนวคิด hybrid เริ่มมีงานในหลายสาขาแล้ว — corpus ปัจจุบัน (80 papers) ยืนยันข้อนี้: [[2026_Hao_Mamba_KAN_HyKANet_EV]], [[2026_Chen_PC_M3_Mamba_EV_Clusters]] และ [[2026_Lahoti_Mamba_3_Sequence_Modeling]] เป็น Mamba line ที่ ingest แล้ว ส่วน novelty ที่ยังยืนยันได้คือคอมโบเต็ม **Mamba backbone + cross-attention + conformalized PICNN head** ตาม [[research_gaps]] (Gap 6, T-7, P-1–P-5) ซึ่งไม่มี paper ใดใน corpus ทำ

## กลุ่ม C: ไอเดียเชื่อมกับ spatial และ operational use

### C1. Dynamic Spatial-Temporal Transformer

เรียนรู้ความสัมพันธ์ระหว่างสถานีแบบ dynamic ตามเวลา แทน static geographic graph

ควรทดสอบใน multi-station dataset โดยเปรียบเทียบ distance graph, correlation graph และ learned dynamic graph

### C2. Hierarchical Probabilistic Transformer

พยากรณ์ระดับ charger, station และ network พร้อมบังคับให้ผลรวมของระดับย่อยสอดคล้องกับระดับบน

อาจใช้ differentiable reconciliation หรือ post-hoc reconciliation ร่วมกับ quantile head

### C3. Forecast-to-Control Evaluation

นำ forecast ไปใช้กับ charging scheduling หรือ V2G dispatch แล้ววัดผลด้าน peak shaving, cost และ battery usage เพิ่มจาก MAE/RMSE

จุดสำคัญคือโมเดลที่ error ต่ำที่สุดอาจไม่ได้ให้ผลควบคุมดีที่สุด

## กลุ่ม D: ไอเดียด้าน robustness และการใช้งานจริง

### D1. Missing/noisy data-aware Transformer

ทดสอบข้อมูลหาย, sensor noise, irregular sampling และสถานีที่มีข้อมูลเริ่มต้นน้อย พร้อมใช้ missingness mask เป็น input

### D2. Cross-station transfer Transformer

pre-train จากสถานีที่มีข้อมูลมาก แล้ว fine-tune สถานีใหม่ที่มีข้อมูลเพียง 3 วัน, 1 สัปดาห์ และ 2 สัปดาห์

เปรียบเทียบ fine-tuning, meta-learning และ zero-shot foundation model

อัปเดตจาก corpus: [[2025_Meyer_Benchmark_Foundation_Models]] (ingest แล้ว) พบว่า foundation models (Chronos, TimesFM) competitive เมื่อ historical data < 4 สัปดาห์ แต่แพ้ supervised model เมื่อข้อมูลเพียงพอ — จึงควรใช้เป็น comparator ในช่วง low-data ของการทดลองนี้

### D3. Calibration under distribution shift

ตรวจว่าช่วง prediction interval ยังมี coverage ถูกต้องหรือไม่เมื่อทดสอบกับฤดูหรือสถานีที่ไม่อยู่ใน training distribution

อาจใช้ conformal calibration เป็นขั้นตอนหลังโมเดล

## การจัดลำดับความเหมาะสม

| Idea | ความใหม่ | ความทำได้จริง | ความสอดคล้องกับผล benchmark | ความเสี่ยง | ลำดับแนะนำ |
|---|---:|---:|---:|---:|---:|
| A1 Peak-aware Probabilistic Transformer | สูง | สูง | สูงมาก | กลาง | 1 |
| A2 Multi-scale Transformer Benchmark | กลาง-สูง | สูงมาก | สูงมาก | ต่ำ | 2 |
| A3 Context-aware Cross-attention | สูง | กลาง-สูง | สูง | กลาง | 3 |
| B1 RevIN + Decomposition | กลาง | สูงมาก | สูง | ต่ำ | 4 |
| B3 Efficient Long-context Transformer | สูง | กลาง | กลาง | กลาง | 5 |
| C1 Dynamic Spatial-Temporal Transformer | สูง | กลาง | ขึ้นกับ dataset | สูง | 6 |
| C2 Hierarchical Probabilistic Transformer | สูงมาก | กลาง-ต่ำ | กลาง | สูง | 7 |
| D1 Robustness to Missing/Noise | กลาง-สูง | สูง | กลาง | ต่ำ | 8 |

## เส้นทาง thesis ที่แนะนำ

### ทางเลือกหลัก: Accuracy + uncertainty

`Baseline Transformer → Multi-scale representation → Peak-aware quantile head → Calibration`

เหมาะที่สุดหากต้องการ thesis ที่มี contribution ชัดและยังอยู่ในขอบเขต Transformer

### ทางเลือกที่สอง: Architecture study

`Transformer / Informer / Autoformer / TFT / PatchTST / iTransformer → controlled tokenization benchmark`

เหมาะหากต้องการงานเชิงทดลองที่น่าเชื่อถือและอธิบายได้ว่าองค์ประกอบใดช่วยในแต่ละ horizon

### ทางเลือกที่สาม: Context and interpretability

`Historical-load encoder + context cross-attention + feature attribution`

เหมาะหากมี weather, price, traffic หรือ session-level covariates ที่มีคุณภาพ

## ข้อเสนอ research questions สำหรับใช้ต่อ

1. How can a Transformer-based model reduce peak underestimation in multi-horizon EV charging load forecasting?
2. Which temporal tokenization strategy provides the best accuracy-efficiency trade-off for EV charging load forecasting?
3. Does cross-attention improve the use of exogenous variables compared with direct feature concatenation?
4. Can probabilistic Transformer forecasts remain calibrated under station-level and seasonal distribution shifts?
5. Does lower forecast error translate into better EV charging scheduling performance?

## ข้อควรตรวจสอบก่อนสรุป novelty

- ควรตรวจ paper ล่าสุดและ preprint เพิ่มก่อนกล่าวว่าแนวคิดใด "ไม่เคยมีใครทำ"
- ~~จำนวน paper ในเอกสารสรุปกับจำนวนไฟล์ใน `raw_sources` ยังไม่สอดคล้องกัน~~ **แก้ไขแล้ว (2026-08-23):** re-ingestion ครบ 80 papers ใน `wiki/papers/` ตรงกับ [[index]] และ [[research_gaps]] ทุกไฟล์ verified
- `dataset_extraction_report.md` มีบางรายการที่ title และ dataset ดูไม่ตรงกัน ควรตรวจ metadata จาก paper ต้นฉบับ
- หมายเหตุ metadata: VMD-Prophet-LSTM (Cheng) เป็นปี **2023** และเป็น hybrid แบบ *centralized* — ไม่ใช่ federated learning; Lyapunov paper อ้างอิงเป็น arXiv:2604.16873 (2026)
- ผล benchmark ปัจจุบันใช้ implementation แบบ Encoder-only ซึ่งแตกต่างจาก architecture ดั้งเดิมของบาง paper จึงควรเรียกว่า controlled reimplementation ไม่ใช่ reproduction เต็มรูปแบบ
- ต้องตรวจ data leakage โดยเฉพาะ weather/price ที่เป็นข้อมูลอนาคต และการ normalization ที่อาจใช้ข้อมูลจาก test period
- ไม่ควรใช้ attention weight เป็นหลักฐานของ causal relationship โดยตรง

## Suggested next experiment

เริ่มจาก A1 แบบ minimal:

1. ใช้ Informer และ Autoformer เป็น backbone ที่ดีที่สุดจาก benchmark
2. เพิ่ม quantile heads สำหรับ P10/P50/P90
3. เปรียบเทียบ MAE loss กับ pinball loss
4. เพิ่ม peak weighting เฉพาะใน target peak zone
5. รายงาน MAE, RMSE, WAPE, Peak Zone WAPE, CRPS, PICP และ Winkler Score
6. ทำ ablation: point vs quantile, weighted vs unweighted, single-scale vs multi-scale

การทดลองชุดนี้จะช่วยตัดสินได้ว่า contribution ที่แท้จริงมาจาก probabilistic output, peak-aware loss หรือ multi-scale representation
