import sys


################ dataset_header #####################
def dataset_header(phase, filename_io):
    '''
    Includes correct header for dataset file!
    '''

    pdiff_header = filename_io + \
'''
None
# Phase : Pdiff
# Traveltime data, xcorr_min =  0.85
# Bandpass filter: /home/sigloch/FFINVERSION/AMPLITUDES/ModelsAndParms/bandpassfilters/gabor/8_30_1.4_0.5
# Register: /import/neptun-radler/AmplitudeProjects/psdata/register_files/register_list
# Station lat_min, lat_max:   -90.00    90.00
# Station lon_min, lon_max:  -180.00   180.00
# Event   lat_min, lat_max:   -90.00    90.00
# Event   lon_min, lon_max:  -180.00   180.00
# Minimum event quality: 3
# Event list:
# local_data_files/0651.2005.065.a
# local_data_files/0732.2008.182.a
# local_data_files/0327.2008.240.a
# local_data_files/0193.2006.244.a
Pdiff
Pdiff
6371  1  1
3480  2  1
6371  3  1
3480  2  1
6371  3  1
3480  2  1
6371  3  1
3480  2  1
6371  5  1
'''

    p_header = filename_io + \
'''
None
# Phase : P
# Traveltime data, xcorr_min =  0.85
# Bandpass filter: /home/sigloch/FFINVERSION/AMPLITUDES/ModelsAndParms/bandpassfilters/gabor/8_30_1.4_0.5
# Register: /import/neptun-radler/AmplitudeProjects/psdata/register_files/register_list
# Station lat_min, lat_max:   -90.00    90.00
# Station lon_min, lon_max:  -180.00   180.00
# Event   lat_min, lat_max:   -90.00    90.00
# Event   lon_min, lon_max:  -180.00   180.00
# Minimum event quality: 3
# Event list:
# local_data_files/0651.2005.065.a
# local_data_files/0732.2008.182.a
# local_data_files/0327.2008.240.a
# local_data_files/0193.2006.244.a
P
P
6371  1  1  # down P
3482  2  1  # turn P
6371  5  1  # last P
'''

    filters = \
'''    
8  # rad. freq/(2*pi*Hz)  abs(gain) (sigma/fc=0.50)
40  # scale=1, 1/fc= 30.0 s
0.061359  0.208349
0.067688  0.263475
0.074671  0.324288
0.082373  0.391374
0.090870  0.465380
0.100243  0.547019
0.110583  0.637080
0.121990  0.736430
0.134573  0.789151
0.148454  0.843454
0.163768  0.903359
0.180660  0.969442
0.199296  0.980665
0.219853  0.977767
0.242531  0.974570
0.267548  0.932762
0.295146  0.881092
0.325591  0.816042
0.359175  0.738778
0.396225  0.657040
0.437095  0.570443
0.482182  0.486244
0.531919  0.407105
0.586787  0.333453
0.647315  0.267503
0.714086  0.210220
0.787744  0.161583
0.869000  0.121975
0.958638  0.090503
1.057522  0.065548
1.166607  0.046454
1.286943  0.032388
1.419692  0.022157
1.566134  0.014864
1.727681  0.009736
1.905893  0.006256
2.102487  0.003950
2.319360  0.002440
2.558603  0.001478
2.822525  0.000876
40  # scale=2, 1/fc= 21.2 s
0.061359  0.075840
0.068264  0.117469
0.075946  0.163782
0.084492  0.215307
0.094000  0.272630
0.104578  0.336404
0.116347  0.407355
0.129439  0.483498
0.144005  0.565266
0.160210  0.656235
0.178239  0.757441
0.198297  0.830464
0.220611  0.893627
0.245437  0.963898
0.273056  0.979569
0.303784  0.997004
0.337969  0.974962
0.376001  0.940985
0.418313  0.881785
0.465386  0.808026
0.517757  0.723370
0.576021  0.632082
0.640842  0.539296
0.712956  0.449195
0.793186  0.364610
0.882445  0.290180
0.981748  0.224382
1.092225  0.170312
1.215135  0.125970
1.351876  0.090855
1.504004  0.064249
1.673252  0.044234
1.861546  0.029768
2.071028  0.019554
2.304084  0.012553
2.563366  0.007863
2.851826  0.004814
3.172746  0.002877
3.529780  0.001680
3.926991  0.000957
40  # scale=3, 1/fc= 15.0 s
0.061359  0.021500
0.068863  0.044351
0.077285  0.069997
0.086737  0.098780
0.097345  0.131083
0.109251  0.167337
0.122612  0.208024
0.137607  0.277861
0.154437  0.356434
0.173324  0.444616
0.194522  0.537026
0.218311  0.633161
0.245011  0.741055
0.274976  0.820395
0.308605  0.906333
0.346347  0.954804
0.388705  0.988349
0.436244  0.996584
0.489596  0.974685
0.549474  0.925854
0.616674  0.855756
0.692093  0.769281
0.776735  0.672822
0.871730  0.572202
0.978342  0.473047
1.097993  0.380670
1.232277  0.297836
1.382984  0.226943
1.552122  0.167953
1.741946  0.120954
1.954985  0.084654
2.194079  0.057688
2.462413  0.038209
2.763565  0.024618
3.101548  0.015446
3.480866  0.009416
3.906574  0.005585
4.384346  0.003222
4.920550  0.001807
5.522331  0.000986
40  # scale=4, 1/fc= 10.6 s
0.061359  0.004747
0.069474  0.014149
0.078662  0.024795
0.089066  0.036849
0.100845  0.050496
0.114182  0.065949
0.129283  0.093543
0.146381  0.139653
0.165741  0.191861
0.187661  0.253250
0.212479  0.335950
0.240581  0.429588
0.272398  0.529921
0.308424  0.641340
0.349214  0.743006
0.395399  0.838079
0.447692  0.917533
0.506900  0.971992
0.573940  0.996240
0.649845  0.989097
0.735790  0.952222
0.833100  0.885497
0.943281  0.798281
1.068033  0.696782
1.209284  0.588863
1.369216  0.481934
1.550300  0.381900
1.755333  0.293116
1.987482  0.217821
2.250333  0.156743
2.547947  0.109240
2.884923  0.073673
3.266464  0.048169
3.698465  0.030486
4.187600  0.018683
4.741425  0.011089
5.368495  0.006374
6.078498  0.003547
6.882401  0.001912
7.792622  0.000998
40  # scale=5, 1/fc=  7.5 s
0.122718  0.021500
0.137727  0.038658
0.154571  0.057916
0.173475  0.079528
0.194691  0.111835
0.218501  0.157120
0.245224  0.207943
0.275215  0.277033
0.308873  0.354785
0.346648  0.444018
0.389043  0.540315
0.436623  0.641704
0.490022  0.741189
0.549951  0.831224
0.617210  0.906873
0.692694  0.961313
0.777411  0.992651
0.872487  0.997479
0.979192  0.974855
1.098947  0.926065
1.233348  0.855792
1.384186  0.769211
1.553471  0.672540
1.743460  0.571938
1.956684  0.472975
2.195985  0.380543
2.464553  0.297760
2.765967  0.226603
3.104244  0.167800
3.483891  0.120814
3.909970  0.084620
4.388157  0.057650
4.924827  0.038198
5.527131  0.024616
6.203096  0.015432
6.961732  0.009412
7.813148  0.005582
8.768693  0.003220
9.841100  0.001807
11.044662  0.000986
40  # scale=6, 1/fc=  5.3 s
0.122718  0.004747
0.138948  0.010662
0.157325  0.017359
0.178132  0.024942
0.201690  0.041097
0.228364  0.062281
0.258566  0.091623
0.292763  0.132730
0.331482  0.186496
0.375321  0.253132
0.424959  0.335015
0.481161  0.429428
0.544796  0.533254
0.616848  0.641635
0.698428  0.746436
0.790797  0.843037
0.895383  0.920402
1.013801  0.974015
1.147879  0.998313
1.299690  0.990827
1.471579  0.952246
1.666201  0.885961
1.886562  0.798321
2.136066  0.696624
2.418568  0.588689
2.738432  0.481729
3.100600  0.381746
3.510665  0.292929
3.974963  0.217685
4.500666  0.156662
5.095895  0.109163
5.769845  0.073671
6.532927  0.048155
7.396930  0.030477
8.375200  0.018679
9.482850  0.011086
10.736991  0.006372
12.156996  0.003547
13.764801  0.001912
15.585245  0.000998
40  # scale=7, 1/fc=  3.7 s
0.184078  0.006245
0.208120  0.012222
0.235302  0.018980
0.266035  0.031005
0.300781  0.047040
0.340066  0.072499
0.384481  0.105950
0.434698  0.150712
0.491473  0.209024
0.555664  0.281527
0.628239  0.367337
0.710292  0.464374
0.803062  0.569386
0.907949  0.676186
1.026535  0.778393
1.160610  0.868879
1.312196  0.939158
1.483580  0.984439
1.677348  0.999692
1.896425  0.984085
2.144114  0.938645
2.424155  0.867590
2.740770  0.777218
3.098739  0.674752
3.503461  0.567673
3.961044  0.462876
4.478391  0.365720
5.063308  0.280083
5.724620  0.207853
6.472306  0.149491
7.317645  0.104193
8.273394  0.070378
9.353971  0.046073
10.575682  0.029228
11.956958  0.017970
13.518642  0.010707
15.284294  0.006183
17.280557  0.003460
19.537549  0.001876
22.089323  0.000986
40  # scale=8, 1/fc=  2.7 s
0.184078  0.001120
0.209966  0.002650
0.239495  0.004395
0.273176  0.008441
0.311595  0.014029
0.355416  0.024163
0.405401  0.039829
0.462415  0.062957
0.527447  0.096177
0.601626  0.141869
0.686236  0.202492
0.782746  0.279095
0.892829  0.371047
1.018393  0.475942
1.161616  0.589197
1.324981  0.703193
1.511322  0.809873
1.723869  0.899925
1.966308  0.964389
2.242842  0.996661
2.558268  0.993790
2.918054  0.955806
3.328438  0.886748
3.796538  0.793536
4.330470  0.684984
4.939491  0.570348
5.634164  0.458076
6.426533  0.354890
7.330337  0.265214
8.361250  0.191179
9.537146  0.132935
10.878417  0.089162
12.408318  0.057686
14.153380  0.036001
16.143861  0.021672
18.414276  0.012584
21.003995  0.007049
23.957922  0.003809
27.327278  0.001985
31.170490  0.000998
'''

    if phase.lower() == 'p':
        complete_header = p_header + filters
        return complete_header
    elif phase.lower() == 'pdiff':
        complete_header = pdiff_header + filters
        return complete_header
    else:
        print 'Invalid phase! %s' %(phase)
        sys.exit(1)

################### source_receiver ##########################
def source_receiver(source, receiver):
    '''
    Create required lines for source and receiver
    '''

    srv = []
    for i in range(len(source)):
        srv.append('20%s %s %s 1 S%s N%s BHZ %s %s %s %s %s %s 1 0 0'
                    %(i, i, i, i, i, 
                        source[i][0], source[i][1], source[i][2], 
                        receiver[i][0], receiver[i][1], receiver[i][2]))
        srv.append('1  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0')
        srv.append('    100  0.9  0.9  1  57.30')
    return srv