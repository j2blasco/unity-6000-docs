* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/sprite-atlas-v2.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprite atlas](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/atlas-landing.html)
  * [Sprite Atlas V2](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)
  * Sprite Atlas V2


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)
Sprite Atlas V2
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/enable-sprite-atlas-v2.html)
Enable Sprite Atlas V2
# Sprite Atlas V2
The original version 1 of the **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) Atlas system packs textures (from sprites, sprites within textures, and sprites in folders) into an Atlas Texture. It packs these textures when it enters Play mode, or when it builds the Player or an AssetBundle. [AssetDatabase V1](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabase.html) can’t have dependencies, and has no importer support for named objects, so Unity packs its Sprite Atlases through a custom mechanism and stores the output data of textures and render data in the `Library/AtlasCache` folder.
**Note:** From Unity 2022.2 onwards, the Editor’s **Sprite Atlas** A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteAtlas) **Mode** is set to **Sprite Atlas V2 - Enabled** by default. Sprite Atlas V2 uses the functionalities exposed by [AssetDatabase V2](https://docs.unity3d.com/2019.3/Documentation/Manual/AssetDatabase.html) (ADBV2) such as [Cache Server](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html) support, which the original Sprite Atlas system didn’t support.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)
Sprite Atlas V2
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/enable-sprite-atlas-v2.html)
Enable Sprite Atlas V2
