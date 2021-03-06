# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        return random.random() <= self.getClearProb()

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        #simple test: randomly determine if virus reproduces or returns error.
        if random.random() <= self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        raise NoChildException()




class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.
        #self.viruses = [v for v in self.viruses if not v.doesClear()]
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        #loop through virus in self.viruses
        #test if doesClear, keep the viruses that do clear.
        #self.viruses = set of viruses that do clear.
        temp = []
        for virus in self.viruses:
            if not virus.doesClear():
                temp.append(virus)
        self.viruses = temp
        #self.viruses = [v for v in self.viruses if not v.doesClear()]

        #calcualte popDensity
        popDensity = len(self.viruses) / float(self.maxPop)

        for virus in self.viruses:
            try:
                #try reproducing
                self.viruses.append(virus.reproduce(popDensity))
            except NoChildException:
                pass
                #if NoChildException is found exit gracefully
        return len(self.viruses)



#
# PROBLEM 3
'''
simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)
done: - instantiates a Patient
done - simulates changes to the virus population for 300 time steps (i.e., 300 calls to update),
- plots the _average_ size of the virus population as a function of time;
   that is, the x-axis should correspond to the number of elapsed time steps,
   and the y-axis should correspond to the average size of the virus population in the patient.
done - The population at time=0 is the population after the first call to update.

done (loop setup) : Run the simulation for numTrials trials, where numTrials in this case can be up to 100 trials.

todo
Use pylab to produce a plot (with a single curve) that displays
  the average result of running the simulation for many trials.
Make sure you run enough trials so that the resulting plot does not
  change much in terms of shape and time steps taken for the average size of the virus population to become stable.
Don't forget to include axes labels, a legend for the curve, and a title on your plot.
'''

#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)

    Part B - Problem 3-1: Running and Analyzing a Simple Simulation (No Drug Treatment)
    """
    #create viruses using input parameters numViruses, maxBirthProb, clearProb
    myPatients = []
    for patient in range(numTrials):
        viruses = []
        for virus in range(numViruses):
            viruses.append(SimpleVirus(maxBirthProb, clearProb))
        myPatients.append(Patient(viruses, maxPop) )
    #
    timeRange = range(300)
    virusPop = [0 for x in timeRange]
    for time_period in timeRange:
        virusSum = 0
        for patient in myPatients:
            virusSum += patient.update()
        virusPop[time_period] = float(virusSum)/numTrials
    #virusPop will record the average virus population of patients at time_period
    #now plot results.
    pylab.plot(timeRange, virusPop, label='virus population')
    pylab.title("virus population over time")
    pylab.xlabel("Time")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = 'best')
    pylab.show()
#
#simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)
#test cases from the sandbox
'''
simulationWithoutDrug(1, 10, 1.0, 0.0, 1)
simulationWithoutDrug(100, 200, 0.2, 0.8, 1)
simulationWithoutDrug(1, 90, 0.8, 0.1, 1)
'''
#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    NB : ResistantVirus(SimpleVirus) inherits SimpleVirus(maxBirthProb, clearProb)
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.

        NB: refer TreatedPatient.getResistPop()

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.

        NB: self.getResistances() returns resistances = A dictionary of drug names
        dictionary.get(key[, default]) : Return the value for key if key is in the dictionary, else default.
        If default is not given, it defaults to None, so that this method never raises a KeyError.
        ie: return the dictionary, then retrieve the value for key=drug.
        ie no key found, return default value of False.
        """
        return self.getResistances().get(drug, False)

    #helper method test resistant to all drugs in a list. simplify coding of reproduce method.
    def isResistantToAll(self, drugList):
        #reuse method isResistantTo via for a in list loop to create array of booleans.
        #all method - returns True only if all elements are True
        return all([self.isResistantTo(drug) for drug in drugList])


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.
        refer : TreatedPatient.update()

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        prob = self.getMaxBirthProb() * (1 - popDensity)
        #check if virus is resistant to all drugs in activeDrugs
        if self.isResistantToAll(activeDrugs) and random.random() < prob:
            #create new local copy of self.resistances we can manipulate
            resistance = self.getResistances()
            for drug in resistance:
                #getMutProb() calculates how often resistance trait will be flipped (True/False)
                if random.random() < self.getMutProb():
                    resistance[drug] = not resistance[drug]
            #returns: a new instance of the ResistantVirus class representing the
            #offspring of this virus particle. The child should have the same
            # maxBirthProb and clearProb values as this virus.
            #ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
            #NB: use new resistance so the randomly flipped resistance is carried forward.
            return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), resistance, self.getMutProb())
        else:
            raise NoChildException


#test cases - keep these, write a test script.
#virus = ResistantVirus(1.0, 0.0, {}, 0.0)
#Testing update() and doesClear(); virus should not be cleared and should always reproduce.
#virus = ResistantVirus(0.0, 0.0, {}, 0.0)
#Testing update() and doesClear(); virus should not be cleared and should never reproduce.
#virus = ResistantVirus(1.0, 1.0, {}, 0.0)
#Testing update() and doesClear(); virus should always be cleared and should always reproduce.
#virus = ResistantVirus(0.0, 1.0, {}, 0.0)
#Testing update() and doesClear(); virus should always be cleared and should never reproduce.
#virus = ResistantVirus(0.0, 1.0, {"drug1":True, "drug2":False}, 0.0)
#Running virus.reproduce(0, []) to make sure that resistances are not changed.
#virus = ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
#Test: child = virus.reproduce(0, ["drug2"])
#Test: child = virus.reproduce(0, ["drug1"])
#virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
#Reproducing 10 times by calling virus.reproduce(0, [])
#virus = ResistantVirus(1.0, 0.0, {"drug2": True}, 1.0)
#Making 100 successive generations and testing their resistance to drug2
#virus = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
#Making 100 successive generations and testing their resistance to drug1.
#virus = ResistantVirus(0.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
#Test: child = virus.reproduce(0, ["drug2"])
#Test: child = virus.reproduce(0, ["drug1"])

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.prescriptions = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.getPrescriptions():
            self.getPrescriptions().append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.prescriptions

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        #NB: drugResist is a list
        """
        from ResistantVirus notes.
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.
        example syntax for dictionary.(should know thisby now)
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
        print "dict['Name']: ", dict['Name']
        """
        resistPop = 0
        for virus in self.getViruses():
            #test if virus has resistance for all drugs in drugResist
            #if all(virus.getResistances()[drug] for drug in drugResist):
            resistPop += virus.isResistantToAll(drugResist)
        """
        resistPop = sum([virus.isResistantToAll(drugResist) \
            for virus in self.getViruses()])
        """
        return resistPop

        #shorthand syntax for above. dislike this as slightly cryptic. same speed.
        #resistPop = sum([virus.isResistantToAll(drugResist) for virus in self.getViruses()])

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        #loop through virus list.
        temp = []
        #test if virus survives (use doesClear method)
        for virus in self.getViruses():
            if not virus.doesClear():
                temp.append(virus)
        self.viruses = temp
        #from simplevirus.reproduce() notes.
        #popDensity: the population density (a float), defined as the current
        # virus population divided by the maximum population.
        popDensity = len(self.getViruses()) / float(self.getMaxPop())
        #test if virus should reproduce and if drugs administered allow virus to reproduce.
        #get copy of this Patient's virus and store
        viruses = self.getViruses()[:]
        #sneaky trick - converts list to array?
        #loop through self.viruses, test each virus for reproductiong and add to virus list.
        for virus in self.getViruses():
            try:
                viruses.append(virus.reproduce(popDensity, self.getPrescriptions()))
            except NoChildException:
                #if virus.reproduce fails this virus did not append a child to the list.
                pass
            #we know the method ResistantVirus.reproduce throws NoChildException, so catch & control the error.
        #store the result in the object
        self.viruses = viruses

        return len(self.getViruses())

        #https://docs.python.org/2/tutorial/errors.html    try  except pass

        """
        SimpleVirus.reproduce(popDensity)
        #returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        ResistantVirus.reproduce(popDensity, activeDrugs)
        """

"""
#test script
print "test 1"
virus = ResistantVirus(1.0, 0.0, {}, 0.0)
patient = TreatedPatient([virus], 100)
print "type(patient.getViruses())=", type(patient.getViruses())
print "type(patient.getViruses()[:])=", type(patient.getViruses()[:])
#Updating patient for 100 time steps
for i in range(10):
    patient.update()
    print patient.getTotalPop()

print "test 2"
virus = ResistantVirus(1.0, 1.0, {}, 0.0)
patient = TreatedPatient([virus], 100)
for i in range(10):
    patient.update()
    print patient.getTotalPop()

#Test for adding duplicate prescriptions in TreatedPatient
#Test addPrescription and getPrescription in TreatedPatient.
#patient = TreatedPatient([], 100)
"""

#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    # TODO
