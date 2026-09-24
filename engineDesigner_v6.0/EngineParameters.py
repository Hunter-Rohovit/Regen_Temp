# --- 1. PROPELLANTS ---
fuel = "RP-1"
oxidizer = "LOX"

# --- 2. OPERATING CONDITIONS ---
Pc = 250.0             # psia, Chamber Pressure
Pe = 7.0               # psia, Exit Pressure (for perfect expansion)
T_target = 3174.0      # lbf, Target Actual Thrust
MR = 2.2               # Mixture Ratio
Cstar_eff = 0.9        # C* Efficiency 
Cf_eff = 0.95          # Cf Efficiency 
mdot = 6               #kg/s, mass flow rate

# --- 3. Coolant Conditions --- 
coolant = "RP-1"
T_cool_in = 298.15 #K, coolant inlet temperature
P_cool_out = Pc*1.24 #Desired Pressure of Coolant before injector, 24% injector stiffness

# --- 4. Materials ---
TCA_material = "GRCop-42"

