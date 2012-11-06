def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0

# Uncertainty
sig = .00000001

print 'measurements: ' + str(measurements)
print 'motion: ' + str(motion)

for i in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    print '%d update:\t mu: %.3f\tsigma: %.3f\tmeasurement: %f' % (i + 1, mu, sig, measurements[i])
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)
    print '%d predict:\t mu: %.3f\tsigma: %.3f\tmotion: %f' % (i + 1, mu, sig, motion[i])



