# Enhanced Disease Information
# Structure:
# - description: Brief summary
# - overview: Detailed explanation (for deep dive)
# - symptoms: Visible signs
# - prevention: List of prevention steps
# - treatment: Quick treatment summary
# - treatment_guidance: Detailed list of actionable treatment steps
# - severity: Level
# - icon: Emoji

RICE_DISEASE_INFO = {
    'Bacterial leaf blight': {
        'description': 'A bacterial disease that causes wilting of seedlings and yellowing and drying of leaves.',
        'overview': 'Bacterial Leaf Blight (BLB), caused by Xanthomonas oryzae pv. oryzae, is one of the most destructive rice diseases in Asia. It causes wilting of seedlings (Kresek phase) and yellowing and drying of leaves (blight phase). The disease reduces grain weight and quality, leading to significant yield losses, especially in high-humidity seasons.',
        'symptoms': 'Water-soaked lesions on leaf edges that turn yellow and dry up. In severe cases, the entire leaf may wilt (Kresek). Milky bacterial ooze may appear on leaf surfaces in the morning.',
        'treatment': 'Use resistant varieties, apply copper-based bactericides, maintain proper water management',
        'prevention': [
            'Use resistant rice varieties suited to your region.',
            'Treat seeds with bleaching powder (100g) and zinc sulfate (2%) before sowing.',
            'Avoid excessive nitrogen fertilizer application; split nitrogen application.',
            'Keep fields clean of weeds and stubble that host the bacteria.',
            'Ensure proper drainage to prevent water stagnation.'
        ],
        'treatment_guidance': [
            'Drain the field immediately if the disease is detected to reduce bacterial spread.',
            'Apply copper-based bactericides (e.g., Copper oxychloride) or Streptocycline during the early stages of infection.',
            'Spray fresh cow dung slurry (20kg/100L water) to control bacterial spread in mild cases.',
            'Burn stubble and straw from infected fields after harvest to kill the pathogen.'
        ],
        'severity': 'High',
        'icon': '🦠'
    },
    'Brown spot': {
        'description': 'A fungal disease causing brown spots on leaves, reducing photosynthesis.',
        'overview': 'Brown Spot is a fungal disease caused by Bipolaris oryzae (formerly Helminthosporium oryzae). It typically infects the leaves and glumes of rice plants, appearing as oval brown spots. The disease is often associated with nutrient-deficient soils (particularly silicon and potassium) and water stress, significantly reducing grain quality and yield.',
        'symptoms': 'Circular to oval brown spots with gray or whitish centers on leaves. Velvety looking spots on grains which cause discoloration.',
        'treatment': 'Use disease-free seeds, apply fungicides, ensure balanced fertilization',
        'prevention': [
            'Use healthy, certified seeds treated with recommended fungicides.',
            'Ensure adequate soil fertility, especially potassium and silicon.',
            'Avoid water stress during critical growth stages (seedling to tillering).',
            'Maintain proper plant spacing for air circulation.',
            'Practice balanced fertilization; avoid nitrogen excess.'
        ],
        'treatment_guidance': [
            'Apply recommended fungicides (e.g., Mancozeb 2.0g/L or Carbendazim 1.0g/L) approved by agricultural authorities at early disease stages.',
            'Improve soil health through organic matter addition and balanced fertilization.',
            'Treat seeds with fungicides like Captan or Thiram (4g/kg) before planting.',
            'Implement proper water management to avoid drought stress which aggravates the disease.'
        ],
        'severity': 'Medium',
        'icon': '🟤'
    },
    'Leaf smut': {
        'description': 'A fungal disease that produces black powdery masses on leaves.',
        'overview': 'Leaf Smut, caused by the fungus Entyloma oryzae, is characterized by small, black, slightly raised spots on the leaves. While generally considered a minor disease, severe widespread infection can lead to leaf senescence and reduced photosynthesis, impacting overall plant health and grain filling.',
        'symptoms': 'Small, black, angular spots on both sides of the leaves. Heavily infected leaves may turn yellow and die prematurely.',
        'treatment': 'Use resistant varieties, remove infected plants, apply appropriate fungicides',
        'prevention': [
            'Use resistant or tolerant rice varieties.',
            'Practice crop rotation to break the disease cycle.',
            'Remove and burn infected plant debris after harvest.',
            'Avoid high rates of nitrogen fertilization which can increase susceptibility.'
        ],
        'treatment_guidance': [
            'In severe cases, spray fungicides such as Propiconazole (1ml/L) or Hexaconazole.',
            'Remove infected leaves manually in small plots to prevent spread.',
            'Ensure field sanitation by keeping bunds free of weeds.',
            'Maintain optimal water levels; avoid stressing the plants.',
        ],
        'severity': 'Medium',
        'icon': '⚫'
    },
    '_Healthy': {
        'description': 'The plant appears healthy with no visible disease symptoms.',
        'overview': 'The plant shows vigorous growth with green, unblemished leaves. Maintaining this state requires consistent management of nutrients, water, and pest control.',
        'symptoms': 'Green, vibrant leaves with no spots, lesions, or discoloration. Strong stems and uniform growth.',
        'treatment': 'Continue regular care and monitoring',
        'prevention': [
            'Maintain regular irrigation schedules.',
            'Apply balanced fertilizers based on soil test recommendations.',
            'Scout the field weekly for any early signs of pests or diseases.',
            'Keep the field free from weeds.'
        ],
        'treatment_guidance': [
            'Continue standard Good Agricultural Practices (GAP).',
            'Monitor weather conditions; high humidity may require preventative action.',
            'Ensure seeds for the next season are stored properly.',
            'Record growth milestones for future reference.'
        ],
        'severity': 'None',
        'icon': '✅'
    }
}

# Pulse Disease Information
PULSE_DISEASE_INFO = {
    'Angular-Leaf-Spot': {
        'description': 'A fungal causing angular spots on leaves, often limited by leaf veins.',
        'overview': 'Angular Leaf Spot (ALS) is caused by the fungus Phaeoisariopsis griseola. It is a major constraint to bean production, causing premature defoliation and yield losses. The disease is seed-borne and survives in crop debris.',
        'symptoms': 'Spots on leaves are angular, brown to gray, and restricted by veins. On pods, spots are circular with reddish-brown centers.',
        'treatment': 'Apply copper fungicides, rotate crops, use disease-free seeds.',
        'prevention': [
            'Use certified disease-free seeds.',
            'Implement a 2-3 year crop rotation with non-legume crops (e.g., maize, cereals).',
            'Plow under infected crop residue immediately after harvest.',
            'Avoid overhead irrigation to reduce humidity.'
        ],
        'treatment_guidance': [
            'Apply copper-based fungicides or Benomyl at the first sign of disease.',
            'Repeat fungicide application every 10-14 days if conditions remain favorable for disease.',
            'Remove and destroy volunteer bean plants in the field.',
            'Do not work in the fields when plants are wet to avoid spreading spores.'
        ],
        'severity': 'Medium',
        'icon': '🍂'
    },
    'Bacterial-Pathogen': {
        'description': 'Bacterial infection affecting the plant foliage.',
        'overview': 'Bacterial blights (Common, Halo) are serious diseases caused by Xanthomonas and Pseudomonas species. They thrive in warm, wet conditions and can spread rapidly through rain splash and wind.',
        'symptoms': 'Water-soaked lesions on leaves that enlarge and turn brown. Leaves may appear "burned". Yellow halos often surround active lesions.',
        'treatment': 'Copper-based bactericides, remove infected debris.',
        'prevention': [
            'Plant resistant varieties if available.',
            'Use disease-free seeds from arid regions.',
            'Rotate crops for at least 2 years.',
            'Control weeds that may serve as alternative hosts.'
        ],
        'treatment_guidance': [
            'Apply copper sprays (Copper Hydroxide) during flowering to pod formation stages.',
            'Remove severely infected plants to reduce inoculum source.',
            'Avoid cultivation or movement through the field when foliage is wet.',
            'Deep plow residues to encourage decomposition.'
        ],
        'severity': 'High',
        'icon': '🦠'
    },
    'Cercospora-Leaf-Spot': {
        'description': 'A fungal disease causing circular spots with reddish margins.',
        'overview': 'Cercospora Leaf Spot is a fungal disease that thrives in warm, humid weather. It attacks leaves, stems, and pods, causing defoliation and reduced pod quality.',
        'symptoms': 'Circular to irregular spots with gray centers and reddish-purple borders. Premature leaf drop.',
        'treatment': 'Fungicidal sprays, remove crop residue, crop rotation.',
        'prevention': [
            'Rotate with cereals like corn or sorghum.',
            'Use wider row spacing to improve air circulation.',
            'Destroy crop residues after harvest.',
            'Select high-quality, pathogen-free seeds.'
        ],
        'treatment_guidance': [
            'Apply systematic fungicides like Azoxystrobin or Chlorothalonil.',
            'Begin spray program at flowering if weather favors disease.',
            'Monitor fields regularly for initial symptoms on lower leaves.',
            'Manage irrigation to minimize leaf wetness duration.'
        ],
        'severity': 'Medium',
        'icon': '🔴'
    },
    'Potassium-Deficiency': {
        'description': 'Nutrient deficiency typically causing yellowing at leaf edges.',
        'overview': 'Potassium (K) deficiency affects water regulation, enzyme activation, and stress tolerance in plants. It initially appears on older leaves as mobile K moves to new growth.',
        'symptoms': 'Chlorosis (yellowing) followed by necrosis (scorching) at leaf margins. Stunted growth and weak stems.',
        'treatment': 'Apply potassium-rich fertilizers (Potash).',
        'prevention': [
            'Conduct soil testing before planting to determine nutrient needs.',
            'Maintain optimal soil pH (6.0-6.5) for K availability.',
            'Apply basal rate of potash fertilizer during sowing.',
            'Ensure adequate soil moisture for nutrient uptake.'
        ],
        'treatment_guidance': [
            'Apply Muriate of Potash (MOP) or Sulfate of Potash as a side dressing.',
            'Use foliar sprays of Potassium Nitrate (1-2%) for rapid correction of severe deficiency.',
            'Incorporate compost or manure to improve soil cation exchange capacity (CEC).',
            'Monitor response; new leaves should appear healthy within a week.'
        ],
        'severity': 'Low',
        'icon': '⚠️'
    },
    'No-Disease-Bean': {
        'description': 'The plant appears healthy.',
        'overview': 'The bean plant is developing normally with no signs of biotic or abiotic stress.',
        'symptoms': 'Dark green, fully expanded leaves. Vigorous flowering and pod set.',
        'treatment': 'Maintain regular care.',
        'prevention': [
            'Maintain consistent irrigation regime.',
            'Scout for insects like aphids or bean beetles.',
            'Fertilize according to crop stage requirements.',
            'Mulch to conserve soil moisture.'
        ],
        'treatment_guidance': [
            'Continue with standard management plan.',
            'Prepare for harvest by monitoring pod maturity.',
            'Keep records of successful management practices.',
            'Ensure tools are cleaned to prevent introducing pathogens.'
        ],
        'severity': 'None',
        'icon': '✅'
    }
}
