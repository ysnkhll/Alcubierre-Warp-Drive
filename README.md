# Alcubierre-Warp-Drive :rocket:
A Python implmentation of Alcubierre's metric using Numpy and Matplotlib.

## Implementation:

Alcubierre defines the following,

![vars](https://wikimedia.org/api/rest_v1/media/math/render/svg/59ae8beb08bae255e40962f098bd9ac6f042a3d6)

in which

![equations](https://wikimedia.org/api/rest_v1/media/math/render/svg/a79c6cc361dd5feaff2c768d482263ce5f3c76c6)

with parameters R>0 and σ>0 Alcubierre's metric is written as,

![metric](https://wikimedia.org/api/rest_v1/media/math/render/svg/34fc4fd0c1af54c827eafabc29cb44fa7341c948)

Alcubierre later derives an expression using the extrinsic curvature tensor K<sub>ij</sub> (9)
showing the expansion (12)

θ = v<sub>s</sub> (<sup>x<sub>s</sub></sup> / r<sub>s</sub>)(<sup>df</sup> / dr<sub>s</sub>)

In Python I defined the derivatives of r(s) & f(r<sub>s</sub>) as
```python
def d_rs(x, rho, xs=15):
    return ((x - xs)**2 + rho**2)**(1/2)
    
def d_frs(rs, sigma=8, R=1):
    a = sigma * (np.tanh((R + rs)*sigma)**2 - 1)
    b = sigma * ((np.tanh(-(R - rs)*sigma)**2 - 1) / np.tanh(R * sigma))
    return (-1/2) * (a - b)
```
where θ
```python
def theta(x, p, xs=15, s=8, R=1):
    vs = R
    drs = d_rs(x, p, xs)
    dfrs = d_frs(drs, s, R)

    return vs * ((x - xs) / drs) * dfrs
```

## Refrence:
* Alcubierre, Miguel (1994). "The warp drive: hyper-fast travel within general relativity". Classical and Quantum Gravity. 11 (5): L73–L77. arXiv:[gr-qc/0009013](https://arxiv.org/abs/gr-qc/0009013) Freely accessible. Bibcode:[1994CQGra..11L..73A](http://adsabs.harvard.edu/abs/1994CQGra..11L..73A). doi:[10.1088/0264-9381/11/5/001](https://doi.org/10.1088%2F0264-9381%2F11%2F5%2F001).
* https://en.wikipedia.org/wiki/Alcubierre_drive

###### [Yasin Khalil](www.yasinkhalil.com) [2FC7 638E 1926 F27](https://keybase.io/ysnkhll)
