# -*- coding: utf-8 -*-
"""
@author: Peter Hardisty
"""

# =============================================================================
#%% Library Importation 
# =============================================================================

import os
import pandas as pd
import numpy as np

# =============================================================================
#%%%End: Library Importation 
# =============================================================================

# =============================================================================
#%%Import Data 
# =============================================================================
#change file path to location where shot_data.csv is
os.chdir(r'C:\Users\phard\OneDrive\Email attachments\Documents\Thunder Task')
shot_data_file_path = 'shots_data.csv'
Reference = pd.read_csv(shot_data_file_path)

Team_A_data =pd.DataFrame(columns = ['x','y','fgmade'])
Team_B_data =pd.DataFrame(columns = ['x','y','fgmade'])

Team_A_data = Reference[Reference['team'] == 'Team A']
Team_B_data = Reference[Reference['team'] == 'Team B']

# =============================================================================
#%%%End: Import Data 
# =============================================================================



# =============================================================================
#%% Shot Distribution 
# =============================================================================
#Shot Distribution Team A
Team_A_NC3 = 0
Team_A_C3 = 0
Team_A_2P = 0 
for i in range(len(Team_A_data)):
	if (Team_A_data['y'][i] > 7.8) & (np.sqrt(np.square(Team_A_data['x'][i]) + np.square(Team_A_data['y'][i])) > 23.75):
		Team_A_NC3 += 1	 
	elif (Team_A_data['y'][i] <= 7.8) & (np.sqrt(np.square(Team_A_data['x'][i]) + np.square(Team_A_data['y'][i])) > 22):
		Team_A_C3 += 1
	else:
		Team_A_2P += 1
		
Team_A_2P_percentage = Team_A_2P/len(Team_A_data['fgmade'])
Team_A_NC3_percentage = Team_A_NC3/len(Team_A_data['fgmade'])
Team_A_C3_percentage = Team_A_C3/len(Team_A_data['fgmade'])
		
#Shot Deistribution Team B
Team_B_NC3 = 0
Team_B_C3 = 0
Team_B_2P = 0
Team_B_data_dis = Team_B_data[Team_B_data['fgmade'] != 0].reset_index(drop = True)
Team_B_data = Team_B_data.reset_index(drop = False) 
for i in range(len(Team_B_data)):
	if (Team_B_data['y'][i] > 7.8) & (np.sqrt(np.square(Team_B_data['x'][i]) + np.square(Team_B_data['y'][i])) > 23.75):
		Team_B_NC3 += 1	 
	elif (Team_B_data['y'][i] <= 7.8) & (np.sqrt(np.square(Team_B_data['x'][i]) + np.square(Team_B_data['y'][i])) > 22):
		Team_B_C3 += 1
	else:
		Team_B_2P += 1
		
Team_B_2P_percentage = Team_B_2P/len(Team_B_data['fgmade'])
Team_B_NC3_percentage = Team_B_NC3/len(Team_B_data['fgmade'])
Team_B_C3_percentage = Team_B_C3/len(Team_B_data['fgmade'])
# =============================================================================
#%%%End: Shot Distribution 
# =============================================================================


# =============================================================================
#%% eFG%
# =============================================================================
#eFG% for Team A

#NC3
#FGA
Team_A_data_NC3 = Team_A_data[(Team_A_data['y'] > 7.8) & (np.sqrt(np.square(Team_A_data['x']) + np.square(Team_A_data['y'])) > 23.75)].reset_index(drop = True)

#FGM and 3PM
Team_A_data_NC3_made = Team_A_data_NC3[Team_A_data_NC3['fgmade'] != 0].reset_index(drop = True)

#eFG%
Team_A_NC3 = (len(Team_A_data_NC3_made) + 0.5*(len(Team_A_data_NC3_made)))/(len(Team_A_data_NC3))
		
#C3
#FGA
Team_A_data_C3 = Team_A_data[(Team_A_data['y'] <= 7.8) & (np.sqrt(np.square(Team_A_data['x']) + np.square(Team_A_data['y'])) > 22)].reset_index(drop = True)

#FGM and 3PM
Team_A_data_C3_made = Team_A_data_C3[Team_A_data_C3['fgmade'] != 0].reset_index(drop = True)

#C3 eFG%
Team_A_C3 = (len(Team_A_data_C3_made) + 0.5*(len(Team_A_data_C3_made)))/(len(Team_A_data_C3))
	
#2P
#FGA
Team_A_data_2P = 0

for xi in range(len(Team_A_data)):
	if (((Team_A_data['y'][xi] > 7.8) & (np.sqrt(np.square(Team_A_data['x'][xi]) + np.square(Team_A_data['y'][xi])) > 23.75)) == 0) & ((Team_A_data['y'][xi] <= 7.8) & ((np.sqrt(np.square(Team_A_data['x'][xi]) + np.square(Team_A_data['y'][xi])) > 22)) == 0):
		Team_A_data_2P += 1

#FGM
Team_A_data_2P_made = 0
for xi in range(len(Team_A_data)):
	if (((Team_A_data['y'][xi] > 7.8) & (np.sqrt(np.square(Team_A_data['x'][xi]) + np.square(Team_A_data['y'][xi])) > 23.75)) == 0) & ((Team_A_data['y'][xi] <= 7.8) & ((np.sqrt(np.square(Team_A_data['x'][xi]) + np.square(Team_A_data['y'][xi])) > 22)) == 0) & (Team_A_data['fgmade'][xi] == 1):
		Team_A_data_2P_made += 1
		
#eFG%
Team_A_2P = ((Team_A_data_2P_made) + 0.5*0)/((Team_A_data_2P))

#Combined eFG%
Team_A_eFGP = (Team_A_data_2P_made + 1.5*(len(Team_A_data_NC3_made)+len(Team_A_data_C3_made)))/(len(Team_A_data['fgmade']))






#eFG% for Team B

#NC3
#FGA
Team_B_data_NC3 = Team_B_data[(Team_B_data['y'] > 7.8) & (np.sqrt(np.square(Team_B_data['x']) + np.square(Team_B_data['y'])) > 23.75)].reset_index(drop = True)

#FGM and 3PM
Team_B_data_NC3_made = Team_B_data_NC3[Team_B_data_NC3['fgmade'] != 0].reset_index(drop = True)

#eFG%
Team_B_NC3 = (len(Team_B_data_NC3_made) + 0.5*(len(Team_B_data_NC3_made)))/(len(Team_B_data_NC3))
		
#C3
#FGA
Team_B_data_C3 = Team_B_data[(Team_B_data['y'] <= 7.8) & (np.sqrt(np.square(Team_B_data['x']) + np.square(Team_B_data['y'])) > 22)].reset_index(drop = True)

#FGM and 3PM
Team_B_data_C3_made = Team_B_data_C3[Team_B_data_C3['fgmade'] != 0].reset_index(drop = True)

#eFG%
Team_B_C3 = (len(Team_B_data_C3_made) + 0.5*(len(Team_B_data_C3_made)))/(len(Team_B_data_C3))
	
#2P
#FGA
Team_B_data_2P = 0

for xi in range(len(Team_B_data)):
	if (((Team_B_data['y'][xi] > 7.8) & (np.sqrt(np.square(Team_B_data['x'][xi]) + np.square(Team_B_data['y'][xi])) > 23.75)) == 0) & ((Team_B_data['y'][xi] <= 7.8) & ((np.sqrt(np.square(Team_B_data['x'][xi]) + np.square(Team_B_data['y'][xi])) > 22)) == 0):
		Team_B_data_2P += 1

#FGM
Team_B_data_2P_made = 0
for xi in range(len(Team_B_data)):
	if (((Team_B_data['y'][xi] > 7.8) & (np.sqrt(np.square(Team_B_data['x'][xi]) + np.square(Team_B_data['y'][xi])) > 23.75)) == 0) & ((Team_B_data['y'][xi] <= 7.8) & ((np.sqrt(np.square(Team_B_data['x'][xi]) + np.square(Team_B_data['y'][xi])) > 22)) == 0) & (Team_B_data['fgmade'][xi] == 1):
		Team_B_data_2P_made += 1
		
#eFG%
Team_B_2P = ((Team_B_data_2P_made) + 0.5*0)/((Team_B_data_2P))


#Combined eFG%
Team_B_eFGP = (Team_B_data_2P_made + 1.5*(len(Team_B_data_NC3_made)+len(Team_B_data_C3_made)))/(len(Team_B_data['fgmade']))

# =============================================================================
#%%%End: eFG%
# =============================================================================




# =============================================================================
#%% Deliverables
# =============================================================================
#Deliverables
Team_A_deliverables ={'Percentage of 2P Shots': Team_A_2P_percentage,
					  'Percentage of NC3 Shots': Team_A_NC3_percentage,  
					  'Percentage of C3 Shots':Team_A_C3_percentage,
					  '2P eFG%': Team_A_2P,
					  'NC3 eFG%': Team_A_NC3,
					  'C3 eFG%': Team_A_C3,
					  'Total eFG%': Team_A_eFGP}		 
	
		
Team_B_deliverables ={'Percentage of 2P Shots': Team_B_2P_percentage,
					  'Percentage of NC3 Shots': Team_B_NC3_percentage,  
					  'Percentage of C3 Shots':Team_B_C3_percentage,
					  '2P eFG%': Team_B_2P,
					  'NC3 eFG%': Team_B_NC3,
					  'C3 eFG%': Team_B_C3,
					  'Total eFG%': Team_B_eFGP}

# =============================================================================
#%%%End: Deliverables
# =============================================================================
