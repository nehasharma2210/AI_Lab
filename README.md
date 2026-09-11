# OCEAN GUARDIAN — SIH 2026
## Problem Statement: SIH26143
## Complete 8-Minute Presentation Script | 6 Members

---

## SLIDE & MEMBER MAP

| Member | Slides Covered | Topic | Time |
|--------|---------------|-------|------|
| Member 1 | Title + Slide 1 | Opening + Problem + Proposed Solution | 1:20 |
| Member 2 | Slide 2 (Part 1) | Technical Approach — Data to Spill Mask | 1:20 |
| Member 3 | Slide 2 (Part 2) | Technical Approach — Drift to GIS Dashboard | 1:40 |
| Member 4 | Slide 3 | Feasibility & Viability | 1:10 |
| Member 5 | Slide 4 | Impact & Benefits | 1:00 |
| Member 6 | Slide 5 | Research, References & Conclusion | 1:30 |
| | | **TOTAL** | **8:00** |

---
---

# MEMBER 1 — Opening + Problem + Proposed Solution
## Slides: Title + Slide 1 | ⏱ 0:00 – 1:20

---

Good morning, respected judges and everyone present here.

Every year, hundreds of oil spills occur in our oceans. The damage is enormous — marine life is destroyed, coastal communities lose their livelihoods, and ecosystems take years to recover. But here is the real problem: by the time authorities detect a spill, trace where it came from, and identify which vessel might be responsible — it is often too late to act effectively.

Today, we present **Ocean Guardian** — an AI-powered, end-to-end investigation support system for marine oil-spill detection and probable source-vessel analysis.

Our solution takes Sentinel-1 SAR satellite imagery, detects the oil spill using deep learning, models how the spill has drifted using wind and ocean-current data, estimates the probable origin region and time window, and correlates that with AIS vessel data to produce a ranked list of candidate vessels — all visualized through a GIS dashboard.

Ocean Guardian is not a system that claims to find the exact culprit. It is a decision-support tool that gives maritime authorities faster, clearer and more evidence-based starting points for their investigations.

My teammate will now explain the technical approach behind this.

> *(Hand over to Member 2)*

---
---

# MEMBER 2 — Technical Approach Part 1
## Slide 2 — Data Input → Spill Characterization | ⏱ 1:20 – 2:40

---

Thank you.

Let me walk you through the first half of our technical workflow — from raw satellite data to a characterized oil spill.

Our primary data input is **Sentinel-1 SAR imagery**. SAR — Synthetic Aperture Radar — is particularly well-suited for marine monitoring because unlike optical cameras, it can operate during both day and night and is largely unaffected by cloud cover. This matters because oil spills do not wait for clear weather.

But raw SAR images cannot be fed directly into a model. They contain speckle noise — a type of grainy distortion — and require calibration and normalization to be consistent across different acquisitions. So our first step is preprocessing: speckle noise reduction, radiometric calibration, normalization, and image tiling to prepare the data for the model.

Once the image is preprocessed, we run it through a deep learning segmentation model — specifically **U-Net or DeepLabv3+**. We use segmentation — rather than a simple bounding box — because we need the actual pixel-level spill mask. We need to know the exact shape, area and geometry of the spill, not just a rough region around it.

The output of this stage is a spill mask, the spill's geographic location, its area and geometry, and a confidence score from the model.

This brings us to the next challenge — we know where the spill is right now, but where did it come from? After detecting and characterizing the spill, the next step is to trace its origin. My teammate will explain how we do that.

> *(Hand over to Member 3)*

---
---

# MEMBER 3 — Technical Approach Part 2
## Slide 2 — Drift → AIS → GIS Dashboard | ⏱ 2:40 – 4:20

---

Exactly. Once we have the spill location and geometry, the question is — how did the oil get there, and where did it originate?

Oil on water does not stay in one place. It drifts — pushed by wind and ocean currents. So we bring in two environmental data sources: **ERA5**, which provides hourly wind information, and **Copernicus Marine Service**, which provides ocean-current data.

Using these, we run a **drift model** in two directions.

Forward drift predicts where the spill will move — useful for response teams who need to contain it.

More importantly for our investigation purpose, we run **backward drift — also called hindcasting**. We reverse the drift physics and trace the spill back in time. This gives us a **probable origin region** and an **estimated time window** — meaning, we can say approximately where the spill likely entered the water and during what period.

Now we need to find out which vessel could be associated with that origin. This is where **AIS data** comes in. AIS — Automatic Identification System — is a tracking system that most vessels are required to broadcast. We query AIS data for vessels that were near the probable origin region during the estimated time window.

We then rank these candidate vessels using four factors: proximity and distance to the origin, trajectory similarity when compared against the drift path, time compatibility with the estimated window, and any behavioural anomalies — such as unusual speed changes or AIS signal gaps.

The final output — the spill mask, drift path, probable origin, vessel trajectories and the candidate ranking — is all brought together and displayed on a **GIS dashboard**, giving investigators a clear, spatial picture of everything they need.

I want to be clear: this system does not legally prove which vessel is responsible. It produces a **probable source-vessel ranking based on spatial, temporal and trajectory evidence** — a powerful starting point for any investigation.

My teammate will now talk about the feasibility of building and deploying this system.

> *(Hand over to Member 4)*

---
---

# MEMBER 4 — Feasibility & Viability
## Slide 3 | ⏱ 4:20 – 5:30

---

Thank you.

A natural question at this point is — is this actually buildable and deployable? Let me address that.

On the **feasibility side**, our approach is built on proven, well-established technology. U-Net and DeepLabv3+ are widely used and validated architectures for image segmentation. ERA5 wind data, Copernicus Marine ocean currents, and Sentinel-1 imagery are all publicly accessible. Our prototype uses a lightweight Sentinel-1 oil-spill segmentation dataset suitable for laptop-based ML development, and supporting data — such as AIS and environmental data — can be accessed through APIs or time-based regional subsets. This keeps the prototype practical without requiring expensive infrastructure.

On the **viability side**, the GIS dashboard is designed to be understandable to non-technical users — maritime authority investigators who need actionable information, not raw model outputs. The system reduces manual monitoring effort and speeds up the initial investigation phase significantly.

The architecture is modular, meaning individual components can be updated or replaced without rebuilding the whole system — and it can be integrated into existing maritime workflows.

We have also identified the key challenges and planned for them. **Adoption** is addressed through training and pilot deployments. **Data synchronization** across multiple sources is managed through multi-source alignment. **Model limitations** are handled through continuous improvement and retraining. And **integration** challenges are managed through the modular design.

My teammate will now explain the broader impact of this system.

> *(Hand over to Member 5)*

---
---

# MEMBER 5 — Impact & Benefits
## Slide 4 | ⏱ 5:30 – 6:30

---

Thank you.

Let me now explain who benefits from Ocean Guardian and how.

For **maritime authorities**, the biggest gain is speed and evidence quality. Instead of spending days trying to manually correlate satellite images, vessel logs and environmental data, investigators get a structured, ranked set of candidate vessels with supporting spatial and temporal evidence — right from the dashboard. This makes investigations faster and more targeted.

For **environmental agencies**, earlier detection means earlier response. Containing a spill before it spreads further can significantly reduce environmental damage to marine ecosystems.

For **coastal communities**, whose livelihoods depend on clean water and healthy fisheries, a system that improves spill response and accountability directly protects their long-term interests.

For the **maritime industry**, Ocean Guardian promotes accountability and responsible vessel operation — which benefits law-abiding operators and supports stronger compliance with environmental regulations.

Overall, the system helps shift oil-spill response from reactive and manual to faster, data-driven and evidence-based. The long-term outcome is cleaner oceans, stronger accountability, and a better-protected marine environment.

My teammate will now cover the research that supports our approach.

> *(Hand over to Member 6)*

---
---

# MEMBER 6 — Research, References & Conclusion
## Slide 5 | ⏱ 6:30 – 8:00

---

Thank you.

Our solution is grounded in published research and validated open datasets. Let me briefly walk through the research foundation.

The first area is **Oil Spill Detection using SAR and Deep Learning** — research here validates the use of Sentinel-1 SAR imagery and deep learning segmentation, specifically architectures like U-Net, for automated detection and masking of marine oil spills.

The second area is **Multi-Source Oil Spill and Vessel Tracing** — this body of work demonstrates that combining satellite imagery, AIS data, wind and ocean current information can provide meaningful information about the probable origin of a spill and associated vessels.

The third area is **Robust Segmentation of Noisy SAR Images** — this research addresses the challenge of speckle noise and varying image conditions in SAR data, which directly informs our preprocessing and model choices.

Our supporting datasets include the **Zenodo Sentinel-1 Oil Spill Segmentation Dataset** for training and local prototyping, the **Global Fishing Watch AIS API** for vessel trajectory data, **Copernicus ERA5** for wind data, and **Copernicus Marine Service** for ocean currents.

Now — what is our research gap and innovation?

Existing research largely addresses individual components in isolation — either spill detection, or drift modelling, or vessel tracing. What is less common is a **unified, end-to-end workflow** that integrates AI-based SAR segmentation, physics-based drift backtracking, AIS correlation, explainable candidate-vessel ranking and GIS visualization into one modular investigation-support system. That integration is what Ocean Guardian contributes.

---

**[CLOSING — 15–20 seconds]**

To conclude —

Ocean Guardian is a decision-support system that helps authorities detect oil spills faster, trace their probable origin more systematically, and identify candidate vessels based on real spatial, temporal and trajectory evidence.

**Detect earlier. Trace better. Respond faster. Protect our oceans.**

We are Team LevelUp. Thank you. We are happy to take your questions.

---
---

# PART 2 — REFERENCE & PREPARATION GUIDE

---

## 1. EXACT TIME ALLOCATION

| Member | Section | Time |
|--------|---------|------|
| Member 1 | Opening + Problem + Solution | 1:20 |
| Member 2 | Technical Part 1 | 1:20 |
| Member 3 | Technical Part 2 | 1:40 |
| Member 4 | Feasibility & Viability | 1:10 |
| Member 5 | Impact | 1:00 |
| Member 6 | Research + Conclusion | 1:30 |
| **Total** | | **8:00** |

---

## 2. KEY POINTS EACH MEMBER MUST REMEMBER

**Member 1:**
- Ocean Guardian = decision-support, not a magic culprit-finder
- 3-line summary of the full pipeline: detect → trace → rank

**Member 2:**
- WHY SAR: works day/night, unaffected by clouds
- WHY segmentation (not bounding box): we need spill mask, shape and area
- Preprocessing is needed because raw SAR has speckle noise and calibration issues

**Member 3:**
- ERA5 = wind | Copernicus Marine = ocean currents
- Forward drift = predict where spill goes | Backward drift = trace where it came from
- AIS ranking uses 4 factors: proximity, trajectory similarity, time compatibility, behavioural anomalies
- NEVER say "exact origin" or "exact culprit" — say "probable" every time

**Member 4:**
- Prototype works on laptop using lightweight dataset + APIs
- 4 challenges + 4 strategies — know each pair
- Key word: MODULAR

**Member 5:**
- 4 beneficiaries: maritime authorities, environmental agencies, coastal communities, maritime industry
- Central message: faster + evidence-based response

**Member 6:**
- 3 research areas + 4 datasets — know names clearly
- Research gap: existing work = individual components | Our work = integrated end-to-end workflow
- Closing lines must be delivered confidently and memorized

---

## 3. 10 MOST IMPORTANT LINES — DELIVER THESE CONFIDENTLY

1. "Ocean Guardian is not a system that claims to find the exact culprit. It is a decision-support tool that gives maritime authorities faster, clearer and more evidence-based starting points for their investigations."

2. "SAR can operate during both day and night and is largely unaffected by cloud cover. This matters because oil spills do not wait for clear weather."

3. "We use segmentation — rather than a simple bounding box — because we need the actual pixel-level spill mask. We need to know the exact shape, area and geometry of the spill."

4. "We run backward drift — also called hindcasting. We reverse the drift physics and trace the spill back in time, giving us a probable origin region and an estimated time window."

5. "This system does not legally prove which vessel is responsible. It produces a probable source-vessel ranking based on spatial, temporal and trajectory evidence."

6. "Our prototype uses a lightweight Sentinel-1 oil-spill segmentation dataset suitable for laptop-based ML development, and supporting data can be accessed through APIs or regional subsets."

7. "The architecture is modular, meaning individual components can be updated or replaced without rebuilding the whole system."

8. "Existing research largely addresses individual components in isolation. Our contribution is integrating these into one unified, end-to-end investigation-support workflow."

9. "Ocean Guardian helps shift oil-spill response from reactive and manual to faster, data-driven and evidence-based."

10. "Detect earlier. Trace better. Respond faster. Protect our oceans."

---

## 4. DIFFICULT TECHNICAL TERMS — SIMPLE EXPLANATIONS

| Term | Pronunciation | Simple Explanation |
|------|--------------|-------------------|
| Sentinel-1 SAR | SEN-ti-nel one S-A-R | A European radar satellite that can see through clouds |
| SAR | S-A-R (spell it out) | Synthetic Aperture Radar — uses radio waves, not light |
| Speckle noise | SPEK-ul noise | Grainy distortion naturally present in radar images |
| Radiometric calibration | ray-dee-oh-MET-rik | Adjusting pixel values to be physically accurate |
| U-Net | YOO-net | A deep learning model shaped like the letter U, used for image segmentation |
| DeepLabv3+ | Deep-Lab-v3-plus | Another segmentation model, alternative to U-Net |
| Segmentation | seg-men-TAY-shun | Labelling every pixel of an image — here, which pixels are oil spill |
| ERA5 | E-R-A five | A global weather dataset from ECMWF with hourly wind data |
| Copernicus Marine | ko-PER-ni-kus | European service providing ocean temperature, current and wave data |
| Hindcasting | HIND-kas-ting | Running a model backward in time to find probable past conditions |
| AIS | A-I-S (spell it out) | Automatic Identification System — vessel tracking via radio broadcast |
| GIS | G-I-S (spell it out) | Geographic Information System — software for displaying maps and spatial data |
| Behavioural anomaly | be-HAY-vyur-al | Unusual vessel behaviour like sudden speed change or AIS signal going off |

---

## 5. 15 LIKELY JUDGE QUESTIONS WITH SHORT ANSWERS

### ⭐ MOST IMPORTANT — PREPARE THESE 5 FIRST

**⭐ Q1: How do you know which vessel caused the spill? Can you prove it?**
No, we do not claim legal proof. Our system produces a probable source-vessel ranking based on spatial location, time window and trajectory correlation. The final investigation and legal determination remain with the authorities. We are a decision-support tool, not a legal verdict system.

**⭐ Q2: Why use SAR imagery instead of normal optical satellite images?**
Optical satellites need sunlight and clear skies. SAR uses radar waves, so it works day and night and is largely unaffected by cloud cover — which is critical for ocean monitoring where cloudy conditions are very common.

**⭐ Q3: Why do you need segmentation? Why not just detect the spill with a bounding box?**
A bounding box only tells you a rough area. We need the actual pixel-level mask of the spill to calculate its true area, shape and geometry. These measurements directly feed into the drift model — the more accurate the spill boundary, the more accurate the origin estimate.

**⭐ Q4: What is the difference between forward drift and backward drift?**
Forward drift predicts where the spill will move next — useful for response and containment. Backward drift, or hindcasting, runs the model in reverse to estimate where the oil was before it reached its current location — that gives us the probable origin region and time window.

**⭐ Q5: What if a vessel has turned off its AIS signal?**
A vessel with AIS signal gaps near the estimated origin and time window actually scores higher on the behavioural anomaly factor in our ranking. An unexplained AIS gap is itself treated as a suspicious indicator, not a reason to exclude the vessel.

---

### Other Important Questions

**Q6: What datasets do you use and are they freely available?**
Yes. We use the Zenodo Sentinel-1 Oil Spill Segmentation Dataset for local ML prototyping. Environmental data comes from Copernicus ERA5 and Copernicus Marine Service. AIS data is accessed via the Global Fishing Watch API. All are publicly accessible.

**Q7: Can your prototype run on a laptop?**
Yes. We use a lightweight segmentation dataset for ML training. ERA5, Copernicus Marine and AIS data can be accessed via APIs or regional time-based subsets, so we do not need to download massive global datasets locally.

**Q8: What is your innovation? U-Net and AIS already exist.**
Correct — we are not claiming to invent U-Net, SAR, AIS or drift modelling. Our innovation is system-level: integrating AI-based SAR segmentation, physics-based drift backtracking, AIS correlation and explainable candidate-vessel ranking into one modular end-to-end investigation workflow. That combined pipeline is our contribution.

**Q9: How accurate is your model?**
Our prototype uses the Zenodo Sentinel-1 segmentation dataset for training and validation. We have not claimed a specific accuracy number — the model performance depends on training data volume and conditions. The confidence score output by the model is used as a reliability indicator in the dashboard.

**Q10: How long does the system take to process a new spill?**
Sentinel-1 has a revisit cycle of several days per region. Once new imagery is available, our pipeline can process it in near-real-time — the analysis is automated from ingestion to GIS output. We are not claiming continuous 24/7 satellite monitoring.

**Q11: Can this system work for any ocean region?**
The pipeline is designed to be region-agnostic. As long as Sentinel-1 coverage, ERA5 wind data, Copernicus Marine current data and AIS data are available for the region, the system can be applied there.

**Q12: How do you handle false positives — things that look like oil but are not?**
SAR images can have look-alike features such as natural slicks or low-wind areas. Our preprocessing and segmentation model is trained specifically on oil-spill data to reduce these. The confidence score from the model also signals low-certainty detections so investigators can apply appropriate scrutiny.

**Q13: What happens if the spill has been drifting for a long time?**
The longer the drift duration, the larger the uncertainty in origin estimation. Our system includes an uncertainty estimate alongside the probable origin region — the output is always communicated as a probable region and time window, not an exact point.

**Q14: Is this a web application?**
The GIS dashboard is the user-facing interface. The architecture is modular with a backend processing pipeline and a frontend visualization layer. Full production deployment details are part of our implementation roadmap.

**Q15: Why is this better than what maritime authorities currently use?**
Current approaches are largely manual — satellite images are reviewed by human analysts, vessel logs are checked separately, and there is no integrated tool to combine spill detection, drift analysis and AIS correlation. Ocean Guardian automates this integration and delivers a structured investigation starting point, which saves significant time and effort.

---

## 6. REHEARSAL PLAN

### Week before presentation — 3 sessions minimum

**Session 1 — Individual read-through (30 min)**
Each member reads their script aloud alone.
Goal: be comfortable with the words, especially technical terms.
Focus on terms from the difficult-terms table.

**Session 2 — Full team run-through with timer (20 min)**
All 6 members present in sequence with a stopwatch running.
Do not stop for mistakes — keep going.
Note down which member goes over time.
Target: finish under 8 minutes 30 seconds.

**Session 3 — Final dress rehearsal (20 min)**
Same as Session 2 but standing up, speaking at presentation volume.
Practice handovers — Member 2 → Member 3 handover is the most important.
Each member must be able to deliver their 10 key lines from memory.
Target: finish between 7 minutes 45 seconds and 8 minutes 15 seconds.

### Day of presentation
- Member 3 and Member 6 should arrive most confident — they carry the heaviest content.
- Keep the Q&A answers mentally ready — especially the 5 starred questions.
- If a judge interrupts mid-presentation, answer briefly and continue from where you stopped.
- Do not panic if you go slightly off-script — the key points matter more than exact words.
