# matrice thermique
import numpy as np

A = np.zeros((43, 35))
F = np.zeros(34)
C = np.zeros(42)
B = np.zeros(42)
theta = np.zeros(42)
G=np.zeros((42,42))

#nombre de personne
nbp=1
phipersonne = 80 #flux de 80watt par personne en moyenne 

#irradiance moyenne solaire sur l'année 
irradiance = 200

# Données
cw= 1250
cg = 1000
cc = 1000
cis = 700

# Température
Text = 15
Tc = 15

#emissivité
epsilonc=0.92
epsilonis=0.07
epsilonw = 0.85
epsilong = 0.92

#Phi


wc=0.15
wis=0.2
wg=0.01
ww=0.1
wp=0.05

lambdac=2
lambdais=0.03
lambdag=1.2
lambdaw=0.15

rhoc=2800
rhois=16
rhog=2500
rhow=500

S1=S7=S3=S5=Sf=7.5
S6=5
S4=10
S2=10
Sp=2.5

hint=8
hext=25

#Mur3        
G[0][0]=hext*S1
G[1][1]=lambdais*S3/wis
G[2][2]=lambdais*S3/wis
G[3][3]=lambdac*S3/wc
G[4][4]=lambdac*S3/wc
G[5][5]=hint*S3

#Mur 1
G[6][6]=hint*S1
G[7][7]=lambdais*S1/wis
G[8][8]=lambdais*S1/wis
G[9][9]=lambdac*S1/wc
G[10][10]=lambdac*S1/wc
G[11][11]=hint*S1

#Porte b 
G[12][12]=hint*Sp
G[13][13]=lambdaw*Sp/wp
G[14][14]=hint*Sp

#Cloison mur 4
G[15][15]=hint*S4
G[16][16]=lambdaw*S4/ww
G[17][17]=lambdaw*S4/ww
G[18][18]=hint*S4

#Mur 5
G[19][19]=hext*S5
G[20][20]=lambdais*S5/wis
G[21][21]=lambdais*S5/wis
G[22][22]=lambdac*S5/wc
G[23][23]=lambdac*S5/wc
G[24][24]=hint*S5

#Fenetre
G[25][25]=hext*Sf
G[26][26]=lambdag*Sf/wg
G[27][27]=hint*Sf

#Mur 6
G[28][28]=hext*S6
G[29][29]=lambdais*S6/wis
G[30][30]=lambdais*S6/wis
G[31][31]=lambdac*S6/wc
G[32][32]=lambdac*S6/wc
G[33][33]=hint*S6

#Mur 7
G[34][34]=hint*S7
G[35][35]=lambdais*S7/wis
G[36][36]=lambdais*S7/wis
G[37][37]=lambdac*S7/wc
G[38][38]=lambdac*S7/wc
G[39][39]=hint*S7

# MUR 3
A[1, 1] = 1
A[2, 1] = -1
A[2, 2] = 1
A[3, 2] = -1
A[3, 3] = 1
A[4, 3] = -1
A[4, 4] = 1
A[5, 4] = -1
A[5, 5] = 1
A[6, 5] = -1
A[6, 6] = 1

# MUR 1
A[7, 7] = 1
A[8, 7] = -1
A[8, 8] = 1
A[9, 8] = -1
A[9, 9] = 1
A[10, 9] = -1
A[10, 10] = 1
A[11, 10] = -1
A[11, 11] = 1
A[12, 11] = -1
A[12, 6] = 1

# PORTE 6
A[13, 17] = -1
A[13, 13] = 1
A[14, 13] = -1
A[14, 12] = 1
A[15, 12] = -1
A[15, 6] = 1

# MUR 4
A[16, 17]= -1
A[16, 16] = 1
A[17, 16] = -1
A[17, 15] = 1
A[18, 15] = -1
A[18, 14] = 1
A[19, 14] = -1
A[19, 6] = 1

# MUR 5
A[20, 18] = 1
A[21, 18] = -1
A[21, 19] = 1
A[22, 19] = -1
A[22, 20] = 1
A[23, 20] = -1
A[23, 21] = 1
A[24, 21] = -1
A[24, 22] = 1
A[25, 22] = -1
A[25, 17] = 1

# Fenetre
A[26, 23] = 1
A[27, 23] = -1
A[27, 24] = 1
A[28, 24] = -1
A[28, 17] = 1

# MUR 6
A[29, 25] = 1
A[30, 25] = -1
A[30, 26] = 1
A[31, 26] = -1
A[31, 27] = 1
A[32, 27] = -1
A[32, 28] = 1
A[33, 28] = -1
A[33, 29] = 1
A[34, 29] = -1
A[34, 17] = 1

# MUR 7
A[35, 30] = 1
A[36, 30] = -1
A[36, 31] = 1
A[37, 31] = -1
A[37, 32] = 1
A[38, 32] = -1
A[38, 33] = 1
A[39, 33] = -1
A[39, 34] = 1
A[40, 34] = -1
A[40, 17] = 1
A[41, 6] = 1
A[42, 17] = 1

Ap = A[1:, 1:]
ApT = np.transpose(Ap)


F[0] = irradiance*epsilonis*S3
F[5] = phipersonne*nbp
F[16] = phipersonne*nbp
F[17] = irradiance*epsilonis*S5
F[21] = irradiance*epsilonc*S5
F[22] = irradiance*epsilong*Sf
F[24] = irradiance*epsilonis*S6
F[28] = irradiance*epsilonc*S6
F[33] = irradiance*epsilonc*S7


C[1] = rhois*cis*wis*S3
C[3] = rhoc*cc*wc*S3
C[18] = rhois*cis*wis*S5
C[20] = rhoc*cc*wc*S5
C[25] = rhois*cis*wis*S6
C[27] = rhoc*cc*wc*S6
C[30] = rhois*cis*wis*S7
C[32] = rhoc*cc*wc*S7
C[7] = rhois*cis*wis*S1
C[9] = rhoc*cc*wc*S1
C[14] = rhow*cw*ww*S4

B[0] = Text
B[6] = Text
B[19] = Text
B[25] = Text
B[28] = Text
B[34] = Text

#diag
Gd=np.diag(G)
Cd=np.diag(C)

theta = np.linalg.inv(Ap.T @ G @ Ap) @( Ap.T @ G @ B + F)
print(theta)

#formule et test
#theta = np.linalg.inv(Ap.T.dot(G).dot(Ap)).dot(ApT.dot(G).dot(B))
#print(theta)