#Notes from Hodgkin-Huxley Paper:

	#Gna, Gk = f(time,membrane potential)
	#Ena, Ek, El, Cm, Gl = constants

	#Ionic current is divided into components carried by sodium and potassium ions and a small leakage current.
	#Each component of ionic current is determined by a driving force
		#The driving force is measured as an electrical potential difference and a permeability for that specific ion.

	#Ina = Gna * (E - Ena) where E is membrane potential
	#Ena is an equilibrium potential for Ena - It's the sodium resting membrane potential

	#The influence of membrane potential on permeability can be summarized:
		#1: Depolarization causes a transient increase in sodium conductance and a slower but maintained increase in potassium conductance.
			#Literally just TIC and DOC
		#2: These changes in conductance are graded and can be reversid by repolarizing the membrane.

		#These are results of an action potential.

	#THE NATURE OF PERMEABILITY CHANGES
		##Changes in permeability are dependent on membrane potential
		#Not membrane current
		#If the potential for a specific ion (Ena) is less than membrane potential (E) then the current is inward.
		#If the potential (Ena) gets greater than (E) then the current changes sign but still follows the same time course.
		#If you restore the normal membrane potential it causes the ion conductance to decline to a low value.
		#The permeability changes arise from the effect of the electric field on the distribution or orientation of molecules with a charge or dipole moment.

		#Depolarization allows the carrier molecules to move so that sodium current increases as the membrane potential is reduced. 
			#Remember: Ina = Gna * (E - Ena). If you reduce E then current decreases

		#The first effect of depolarization is a movement of negatively charged molecules from the outside to the inside of the membrane.
			#Gives an initial outward current and an inward current does not occur until combined carriers lose sodium to the internal solution and return to the outside of the membrane.

		#Different hypothesis: Sodium movement depends on the distribution of charged particles which do not act as carriesrs in the usual sense, but which allow sodium to pass through the membrane when they occupy particular sites in the membrane.
			#This means that the rate of movement of particles determines the rate that sodium conductance rises to its max but doesn't affect the max value of Gna.
			#Temperature affects this rate of Gna rise but not its max.
			#Transient nature explanation: The activating particles undergo a chemical change after moving from the position they occupy when the membrane potential is high.

		#Steep relation between ionic conductance and membrane potential.
			#Gna can be increased e-fold by a reduction of only 4mV

	#MEMBRANE CURRENT DURING A VOLTAGE CLAMP

	#1): Divide the total membrane current into Capacitor current and ionic current
		#I = CM * dV/dt + Ii
		#Parallel because of current measurements when dV/dt = 0
			#and setting I=0

	#IONIC Current:

	#Ii = Ina + Ik + Il
	#Individual
		#Ina = Gna(E - Ena)
		#Ik = Gk(E - Ek)
		#Il = Gl(E - El)

		#They change E to V here conveniently

		#V = E - Er
		#Vna = Ena - Er
		#Vk = Ek - Er
		#Vl = El - Er

		#Er = absolute value of the resting potential

	#IONIC CONDUCTANCES

	#Want to find equations that describe the conductances accurately and simply
	#Looks like a charging and then discharging capacitor
	#G = V*I so it's directly proportional to voltage in a capacitor.

	#This is the part of the lectures where Irazoqui talks about a delay in space and time for the charging current
	#They had to use G0 and Ginfinity to compensate.

	#POTASSIUM CONDUCTANCE

	#Gk = Gkbar * n^4
		#dn/dt = alphaSubn * (1 - n) - betaSubn * n
		#Units for Gkbar = conductance / cm^2
		#Alpha and Beta are rate constants that vary with voltage but not with time and have frequency unitys
		#N is dimensionless and varies between zero and one
		
		#Physical basis understanding:
			#Assume that potassium ions can only cross the membrane when four similar particles occupy a certain region of the membrane.
			#n is a proportion of the particles in a certain orientation or position
			#1-n is the proportion that are somewhere else (outside the membrane)
			#Alpha = rate of transfer from outside to inside
			#Beta = rate of transfer from inside to outside
			#Negative charge on particle - Alpha increase, Beta should decrease when membrane is depolarized.

		#N at rest
			#n0 = (alphaSubn0)/(alphaSubn0 + betaSubn0)
			#This means the resting state proportion of particles inside is equal to the proportion of rate outside to inside over the total rates
			


		