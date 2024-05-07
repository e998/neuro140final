### REWRITTEN STARTING FROM:

# ghostAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

from game import Agent
from game import Actions
from game import Directions
from util import *

class GhostAgent(Agent):
    def __init__(self, index):
        self.index = index
    
    def getAction(self, state):
        # Choose action from distribution if move to be made
        dist = self.getDistribution(state)
        if len(dist) == 0:
            return Directions.STOP
        else:
            return chooseFromDistribution(dist)
    
    def getDistribution(self, state):
        # Returns Counter that encodes distribution over 
        # actions from the provided state
        raiseNotDefined()

class RandomGhost(GhostAgent):
    # Ghost chooses Uniformly among legal moves
    def getDistribution(self, state):
        dist = Counter()
        for action in state.getLegalActions(self.index):
            # All legal actions are dist 1 away from current state
            dist[action] = 1.0
        dist.normalize()
        return dist

###
def constructDistribution(legalActions, bestActions, bestProb):
    # Construct distribution for actions
    dist = Counter()
    for action in bestActions:
        dist[action] = bestProb / len(bestActions)
    for action in legalActions:
        dist[action] += (1 - bestProb) / len(legalActions)
    dist.normalize()
    return dist

class DirectionalGhost(GhostAgent):
    # Directed movements: prefers to rush Pacman or flee when scared

    def __init__(self, index, prob_attack=0.8, prob_scaredFlee=0.8):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee
    
    def getDistribution(self, state):
        # Variables obtained from state of agent
        ghostState = state.getGhostState(self.index)
        legalActions = state.getLegalActions(self.index)
        pos = state.getGhostPosition(self.index)
        isScared = ghostState.scaredTimer > 0 # If ghost in scared state

        speed = 1
        if isScared:
            speed = 0.5

        pacmanPos = state.getPacmanPosition()
        actionVectors = [Actions.directionToVector(action, speed) 
                         for action in legalActions]
        newPos = [(pos[0] + action[0], pos[1] + action[1]) 
                  for action in actionVectors]

        # Best ghost actions given state
        # Manhattan dist
        # distToPacman = [manhattanDist(pos, pacmanPos) for pos in newPos]
        ###
        # Euclidean dist
        distToPacman = [euclideanDist(pos, pacmanPos) for pos in newPos]
        if isScared:
            bestScore = max(distToPacman)
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min(distToPacman)
            bestProb = self.prob_attack
        # Move ghost optimally situated
        bestActions = [action for action, dist in 
                       zip(legalActions, distToPacman) if dist == bestScore]
        
        ###
        constructDistribution(legalActions, bestActions, bestProb)

###
class FearfulGhost(GhostAgent):
    # Ghost prefers to flee when scared and less likely to attack
    # Increased speed of flight

    def __init__(self, index, prob_attack=0.2, prob_scaredFlee=0.8):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee
    
    def getDistribution(self, state):
        # Variables obtained from state of agent
        ghostState = state.getGhostState(self.index)
        legalActions = state.getLegalActions(self.index)
        pos = state.getGhostPosition(self.index)
        isScared = ghostState.scaredTimer > 0 # If ghost in scared state

        speed = 1
        if isScared:
            speed = 0.7 # Increased speed 0.5 -> 0.7

        pacmanPos = state.getPacmanPosition()
        actionVectors = [Actions.directionToVector(action, speed) 
                         for action in legalActions]
        newPos = [(pos[0] + action[0], pos[1] + action[1]) 
                  for action in actionVectors]

        # Best ghost actions given state
        # Manhattan dist
        # distToPacman = [manhattanDist(pos, pacmanPos) for pos in newPos]
        ###
        # Euclidean dist
        distToPacman = [euclideanDist(pos, pacmanPos) for pos in newPos]
        if isScared:
            bestScore = max(distToPacman)
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min(distToPacman)
            bestProb = self.prob_attack
        # Move ghost optimally situated
        bestActions = [action for action, dist in 
                       zip(legalActions, distToPacman) if dist == bestScore]
        
        ###
        constructDistribution(legalActions, bestActions, bestProb)

###
class AggressiveGhost(GhostAgent):
    # Ghost prefers to rush Pacman and less likely to flee
    # Decreased speed of flight

    def __init__(self, index, prob_attack=0.8, prob_scaredFlee=0.2):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee
    
    def getDistribution(self, state):
        # Variables obtained from state of agent
        ghostState = state.getGhostState(self.index)
        legalActions = state.getLegalActions(self.index)
        pos = state.getGhostPosition(self.index)
        isScared = ghostState.scaredTimer > 0 # If ghost in scared state

        speed = 1
        if isScared:
            speed = 0.3 # Decreased speed 0.5 -> 0.3

        pacmanPos = state.getPacmanPosition()
        actionVectors = [Actions.directionToVector(action, speed) 
                         for action in legalActions]
        newPos = [(pos[0] + action[0], pos[1] + action[1]) 
                  for action in actionVectors]

        # Best ghost actions given state
        # Manhattan dist
        # distToPacman = [manhattanDist(pos, pacmanPos) for pos in newPos]
        ###
        # Euclidean dist
        distToPacman = [euclideanDist(pos, pacmanPos) for pos in newPos]
        if isScared:
            bestScore = max(distToPacman)
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min(distToPacman)
            bestProb = self.prob_attack
        # Move ghost optimally situated
        bestActions = [action for action, dist in 
                       zip(legalActions, distToPacman) if dist == bestScore]
        
        ###
        constructDistribution(legalActions, bestActions, bestProb)

### Enabling random (including illegal) ghost movements through walls
class RandomGhostTeleportingNearWalls(GhostAgent):
    def __init__(self, index, prob=0.5):
        self.prob = prob
        self.index = index
    
    def getDistribution(self, state):
        dist = Counter()
        # Select between any adjacent positions
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            dist[action] = 1.0
        dist.normalize()
        return dist

###
class MaxMoveGhost(GhostAgent):
    # Directed movements: always attacks or flees given opportunity

    def __init__(self, index, prob_attack=1, prob_scaredFlee=1):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee
    
    def getDistribution(self, state):
        # Variables obtained from state of agent
        ghostState = state.getGhostState(self.index)
        legalActions = state.getLegalActions(self.index)
        pos = state.getGhostPosition(self.index)
        isScared = ghostState.scaredTimer > 0 # If ghost in scared state

        speed = 1
        if isScared:
            speed = 0.5

        pacmanPos = state.getPacmanPosition()
        actionVectors = [Actions.directionToVector(action, speed) 
                         for action in legalActions]
        newPos = [(pos[0] + action[0], pos[1] + action[1]) 
                  for action in actionVectors]

        # Best ghost actions given state
        # Manhattan dist
        # distToPacman = [manhattanDist(pos, pacmanPos) for pos in newPos]
        ###
        # Euclidean dist
        distToPacman = [euclideanDist(pos, pacmanPos) for pos in newPos]
        if isScared:
            bestScore = max(distToPacman)
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min(distToPacman)
            bestProb = self.prob_attack
        # Move ghost optimally situated
        bestActions = [action for action, dist in 
                       zip(legalActions, distToPacman) if dist == bestScore]
        
        ###
        constructDistribution(legalActions, bestActions, bestProb)
