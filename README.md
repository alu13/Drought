# Drought Simulation

Drought is a massive issue in Southern California, and a big reason is agriculture (80% of human freshwater usage). 
Many of the crops grown in california (almonds, grapes, etc.) require an unsustainable amount of freshwater. 

This project is split into two parts:

## Drought Analysis

This first part uses simple analytics to see if drought has legitamitely been worsening in the SoCal area over the past ~100 years.
1. Simple windowed trend techniques to find patterns
2. Other correlation analysis/simple algorithms

## Crop Composition Analysis

The second part is a discrete simulation of how crop composition affects the groundwater capacity in SoCal. Tthe only variables are crop composition and their expected water consumption, small variance rainwater, and the current groundwater store.
Obbiously more water-efficient crops = more groundwater, but the simulation is useful to visualize just how much change is necessary to be sustainable.


The entire project can be seen in the ipynb file in /src/Drought.ipynb
