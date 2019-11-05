---
layout: post
title: "An Intuitive Understanding of Fourier Transform"
date: 2017-10-19 10:23
---
Fourier transform is really widely-used in digital signal processing. I use it for frequency domain analysis in my research papers, but actually I always have little knowledge about how it works and what is the theory behind.

$$
F(\omega) = \int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt
$$

This is a very common definition of Fourier transform, there are also a plenty of resources on the internet explaining it and using it. However, the more intuitive explanation is its inverse transform:

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty}F(\omega)e^{i\omega t}\,d\omega
$$

Now, we begin with the simplest form of moving around a circle [^1]:

$$
f(t) = Re^{i\omega t}
$$

Here, $R$ is the radius of circle and $\omega$ can be seen as the angular frequency. Now, if we have two circles, one at the end of the other, the position turns to:

$$
f(t) = R_1 e^{i \omega_1 t} + R_2 e^{i \omega_2 t}
$$

Now, we can have three, four or infinitely-many circles at the meantime:

$$
f(t) = \int_{-\infty}^{\infty}R(\omega)e^{i \omega t}\,d\omega
$$

> We can trace any path using a system of wheels, that is, wheels on wheels on wheels...

Therefore, you can trace any time-dependent path using infinitely circles of different radii and frequencies.

Specially, if your path closes on itself, the Fourier transform turns out to simplify to a Fourier series:

$$
f(t) = \sum_{k=-\infty}^{\infty}c_k e^{ik\omega_0t}
$$

where $\omega_0$ is the angular frequency of the slowest circle.

-----

- [Fourier Transform Clarified](http://blog.ivank.net/fourier-transform-clarified.html)
- [Fourier transform for dummies](https://math.stackexchange.com/questions/1002/fourier-transform-for-dummies)
- [The Scientist and Engineer's Guide to Digital Signal Processing](http://www.dspguide.com)
- [Ptolemy and Homer (Simpson)](http://www.youtube.com/watch?v=QVuU2YCwHjw)

[^1]: If you have confusion about this representation, think about Euler's formula: $e^{it}={\cos}t+i{\sin}t$.
