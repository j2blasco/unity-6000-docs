* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-TechnicalInformation.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Lighting data](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmap-data-landing.html)
  * Light Probe data format


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmaps-TechnicalInformation.html)
Lightmap data format
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
Precalculating surface lighting with lightmaps
# Light Probe data format
The lighting information in the **light probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) are encoded as Spherical Harmonics basis functions. We use third order polynomials, also known as L2 Spherical Harmonics. These are stored using 27 floating point values, 9 for each color channel.
The **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) implementation in Unity uses a different spherical harmonics approach than Geomerics, the feature’s original developer, namely the notation and reconstruction method from Peter-Pike Sloan’s paper, [Stupid Spherical Harmonics (SH) Tricks](http://www.ppsloan.org/publications/StupidSH36.pdf). Geomerics’ original approach was based on the notation and reconstruction method from Ramamoorthi/Hanrahan’s paper, [An Efﬁcient Representation for Irradiance Environment Maps](http://cseweb.ucsd.edu/~ravir/papers/envmap/envmap.pdf).
The **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code for reconstruction is found in UnityCG.cginc and is using the method from Appendix A10 Shader/CPU code for Irradiance Environment Maps from Peter-Pikes paper.
The data is internally ordered like this:
```
                        [L00:  DC]

            [L1-1:  y] [L10:   z] [L11:   x]

  [L2-2: xy] [L2-1: yz] [L20:  zz] [L21:  xz]  [L22:  xx - yy]

```

The 9 coefficients for R, G and B are ordered like this:
```
L00, L1-1,  L10,  L11, L2-2, L2-1,  L20,  L21,  L22, // red channel

L00, L1-1,  L10,  L11, L2-2, L2-1,  L20,  L21,  L22, // blue channel

L00, L1-1,  L10,  L11, L2-2, L2-1,  L20,  L21,  L22  // green channel

```

For more “under-the-hood” information about Unity’s light probe system, you can read Robert Cupisz’s talk from GDC 2012, [Light Probe Interpolation Using Tetrahedral Tessellations”, GDC 2012](http://gdcvault.com/play/1015312/Light-Probe-Interpolation-Using-Tetrahedral)
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmaps-TechnicalInformation.html)
Lightmap data format
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
Precalculating surface lighting with lightmaps
