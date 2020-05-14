#!/usr/bin/env python
# coding: utf-8

# In[8]:


import torch 
import numpy as np
import random

action_dim = 5 # 5 possible actions 
pos_dim    = 2 # x and y coordinates


# In[14]:


# environment is of size 8*8
# size of patch is 2*2
# so coordinates are go from [0,0] to [3,3]


def move(batch_size, num_times_agent_moves):
    
    actions_one_hot = np.zeros((batch_size,action_dim, num_times_agent_moves - 1), np.int32) # 4x5x99
    action = np.zeros((batch_size, num_times_agent_moves-1), np.int32)
    position = np.zeros((batch_size, pos_dim, num_times_agent_moves), np.int32)


    

    for batch_size_index in range(batch_size):

        for time_step in range(num_times_agent_moves) :

            if time_step == 0 : # beginning

                position[batch_size_index,:,time_step] = np.ones(2) * 2
                # agent will start from middle

            else :

                while(True):

                    action_random = random.randint(0,4)

                    # 0 -> move right 
                    # 1 -> move left
                    # 2 -> move up
                    # 3 -> move down
                    # 4 -> do not move 

                    if action_random == 0 : # move right
                    # we need to check that the agent is not at right extreme of the environment

                        if position[batch_size_index,1,time_step-1] == 3 : # agent is at the extreme right
                            continue # choose a new random action agent cannot move right 

                        else :
                            position[batch_size_index,:,time_step]  = position[batch_size_index,:,time_step-1] + np.array([0,1])
                            action[batch_size_index,time_step-1] = action_random # agent to move right at next step (i.e. time_step)
                            break # break the while loop and go to next time step.

                    if action_random == 1 : # move left
                        # we need to check that the agent is not at extreme left of the environment
                        
                        if position[batch_size_index,1,time_step-1] == 0 :
                            continue               
                        
                        else :      
                            position[batch_size_index,:,time_step] = position[batch_size_index,:,time_step-1] + np.array([0,-1])
                            action[batch_size_index,time_step-1] = action_random
                            break
                            
                    if action_random == 2 : # move up
                        # we need to check that the agent is not at the top of the environment
                        
                        if position[batch_size_index,0,time_step-1] == 0 : # agent is at the top
                            continue
                            
                        else :   
                            position[batch_size_index,:,time_step] = position[batch_size_index,:,time_step-1] + np.array([-1,0])
                            action[batch_size_index,time_step-1] = action_random
                            break
                            
                    if action_random == 3 :
                        # we need to check that the agent is not at the bottom of the environment
                        
                        if position[batch_size_index,0,time_step-1] == 3 : #agent is at the bottom
                            continue
                            
                        else :
                            position[batch_size_index,:,time_step] = position[batch_size_index,:,time_step-1] + np.array([1,0])
                            action[batch_size_index,time_step-1] = action_random
                            break
                            
                    if action_random == 4 : # agent to stay at the same position
                        
                        position[batch_size_index,:,time_step] = position[batch_size_index,:,time_step-1]
                        action[batch_size_index,time_step-1] = action_random
                        break
                        

    # converting actions to one hot actions
    # one hot actions have size batch_size * 5 * num_time_agent_moves
    
    
    
    for batch_size_index in range(batch_size) :
        print(batch_size)
        print(batch_size_index)
        print(num_times_agent_moves)
        
        actions_one_hot[batch_size_index,action[batch_size_index], np.array(range(num_times_agent_moves-1))] = 1
        
    actions_one_hot = torch.from_numpy(actions_one_hot) # converting to a tensor as mathematical operations are easy with tensors
    
    return actions_one_hot, position, action  
