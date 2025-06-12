* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Creating models outside of Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingDCCAssets.html)
  * Model file formats


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingDCCAssets.html)
Creating models outside of Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/HOWTO-ImportObjectsFrom3DApps.html)
Support for proprietary model file formats
# Model file formats
Unity supports a number of standard and proprietary **model file** formats.
Internally, Unity uses the .fbx file format as its importing chain. It is best practice to use the .fbx file format whenever possible, and you should not use proprietary model file formats in production.
## Supported model file formats
### Standard file formats
Unity can read the following standard 3D file formats: 
  * [.fbx](https://www.autodesk.com/products/fbx/overview)
  * [.dae (Collada)](https://www.khronos.org/collada/)
  * .dxf
  * .obj.


These file formats are widely supported. They are also often smaller than the proprietary equivalent, which makes your project size smaller, and faster to iterate over.
You can also also re-import exported .fbx or .obj files into your 3D modeling software of choice to check that all of the information has been exported correctly.
### Proprietary file formats
You should not use these file formats in production; instead, export to the .fbx format wherever possible. However, sometimes you might need to include these files as part of your project.
Unity can import proprietary files from the following 3D modeling software, and then convert them into .fbx files:
  * [Autodesk Maya](https://www.autodesk.com/products/maya/overview)
  * [Blender](https://www.blender.org/)
  * [Modo](https://www.foundry.com/products/modo)
  * [Cheetah3D](https://www.cheetah3d.com/)


For more information, see [Importing proprietary model files into Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/HOWTO-ImportObjectsFrom3DApps.html).
The following applications do not use .fbx as an intermediary. Unity must convert them into .fbx files before importing them into the Editor:
  * [SketchUp](https://www.sketchup.com/)
  * [SpeedTree](https://store.speedtree.com/unity/)
  * [Autodesk® 3ds Max®](https://www.autodesk.com/products/3ds-max/overview)


For more information, see the documentation on [SketchUp Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SketchUpImporter.html) and [SpeedTree Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpeedTreeImporter.html).
## Unsupported model file formats
Unity does not provide built-in support for Cinema4D files. To use Cinema4D files in Unity, you should export them from the proprietary software as .fbx files.
Assets saved as .ma, .mb, .max, .c4d, or .blend files fail to import unless you have the corresponding 3D modeling software installed on your computer. This means that everybody working on your Unity project must have the correct software installed. For example, if you use [the Autodesk Maya LT license](https://www.autodesk.com/products/maya-lt/overview) to create an .mb file and copy it into your project, anyone else that opens your project also needs to have Autodesk Maya LT installed on their computer.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingDCCAssets.html)
Creating models outside of Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/HOWTO-ImportObjectsFrom3DApps.html)
Support for proprietary model file formats
