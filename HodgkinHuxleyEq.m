clc;
clear all;

a = 0.001;
ro = 3;
ri = 4;
v = 10;

z = 14;
t = 25;

Vm = MembraneVoltage(z,t);
dVmdt = 40;
d2Vmdt2 = 30;

Vk = -0.065;
Vna = 0.020;
Vl = 0.001;

alphaK = (-0.01 * (Vm + 50)) / (exp(-0.01 * (Vm + 50)));
betaK = 0.125 * exp(-0.0125 * (Vm + 50));
tauK = 1 / (alphaK + betaK);

alphaNa = Va * 10;
betaNa = Va + 35;
tauNa = 1 / (alphaNa + betaNa);

Gk = PotassiumConductance(Vm,t);
Gna = SodiumConductance(Vm,t);
Gl = 4;

Cm = 20;

Jc = Cm * dVmdt;
Jk = Gk * (Vm - Vmk);
Jna = Gna * (Vm - Vmna);
Jl = Gl * (Vm - Vl);

Jm = Jc + Jk + Jna + Jl;

Km = 2 * pi * a * Jm;


