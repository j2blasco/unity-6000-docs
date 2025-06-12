* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/models-preparing.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Creating models outside of Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingDCCAssets.html)
  * Preparing your model files for export


[](https://docs.unity3d.com/6000.0/Documentation/Manual/HOWTO-ImportObjectsFrom3DApps.html)
Support for proprietary model file formats
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ModelingOptimizedCharacters.html)
Creating models for optimal performance
# Preparing your model files for export
## Scaling factors
Unity’s physics and lighting systems expect **1** meter in the game world to be **1** unit in the imported **Model file** A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Modelfile).
The defaults for different 3D packages are as follows:
  * .fbx, .max, .jas = **0.01**
  * .3ds = **0.1**
  * .mb, .ma, .lxo, .dxf, .blend, .dae = **1**


When importing Model files into Unity from a 3D modeling application with a different scaling factor, you can convert the file units to use the Unity scale by enabling the [Convert Units](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#scene) option.
## Optimizing your files
Before you import your files into Unity, there are a number of steps you should follow to ensure that your files are optimized in the best way.
Think about what you want to export: some **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) objects are essential but others might be unnecessary, so you can optimize the data in Unity by keeping only the essential objects. This helps remove unwanted data from your scene, and also means you can use a preset or custom scene exporter to automate or simplify the export process.
### Preparing what you need to include
The following table outlines special considerations you should make for each asset type to work most optimally in Unity:
**Object** | **Preparations**  
---|---  
**Meshes** | All NURBS, NURMS, splines, patches, and subdiv surfaces must be converted to polygons (triangulation or quadrangulation)  
**Bake deformers** | Make sure that you bake deformers onto the models in your application before exporting to the .fbx file format. For example, if you want to export a complex rig from Maya, you can bake the deformation onto skin weights before you export the Model to .fbx.  
**Textures** | Make sure the textures in your application are either sourced from your Unity Project, or copy them into a folder called `Textures` inside your Unity Project.   
  
**Note:** Don’t use the **Embed Media** option to embed textures into the .fbx file. Because Unity has to extract the textures before it uses them, embedding them enlarges your project and slows the import process.  
**Smoothing** | If you want to import blend shape normals, you must have smoothing groups in the .fbx file.  
### Setting the .fbx export options
Before you export the .fbx file, make sure that you use the latest .fbx exporter version that your 3D modeling application supports. When you export to .fbx, make a note of each setting in the export dialog of your 3D modeling application so that you can match up the .fbx import settings in Unity. Most .fbx exporters allow you to enable or disable exporting of certain animations, **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), and lighting effects, so if anything is missing when you import it into Unity, check to see if it was exported. 
## Verifying and importing into Unity
Before importing your .fbx file into Unity, verify the size of your exported file. Perform a sanity check on the file size (for example, to see if it is larger than 10KB). Re-import your .fbx file back into the 3D modeling software you used to generate it (for example, into a new scene). Check to make sure it is what you expected.
To import your file into Unity, follow the instructions for [Importing](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html), keeping in mind how you set the export options in your 3D modeling software.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/HOWTO-ImportObjectsFrom3DApps.html)
Support for proprietary model file formats
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ModelingOptimizedCharacters.html)
Creating models for optimal performance
