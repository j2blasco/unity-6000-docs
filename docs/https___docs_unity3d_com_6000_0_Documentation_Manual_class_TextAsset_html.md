* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Importing assets](https://docs.unity3d.com/6000.0/Documentation/Manual/import-assets.html)
  * Text assets


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptedImporters.html)
Managing importers with scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html)
Supported asset type reference
# Text assets
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html "Go to TextAsset page in the Scripting Reference")
Text assets are a format for imported text files. When you drop a text file into your `Project` folder, Unity converts it to a Text Asset. The supported text formats are:
  * `.bytes`
  * `.csv`
  * `.fnt`
  * `.htm`
  * `.html`
  * `.json`
  * `.md`
  * `.txt`
  * `.xml`
  * `.yaml`


**Note:** When you use [`AssetDatabase.FindAssets`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html) with the `t:TextAsset` filter, script files are also considered a text asset, and are included in the results.
If you select a text asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), the [Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html) displays the text content of the file.
## Using text assets
Text assets are useful for getting text from different text files into your application while you’re building it. For example, you can use it to add a `.txt` file to your project to bring the text into your application. If you’re making a text-heavy adventure game, you can put the text for each **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) separate `.txt` files and reference the text asset when a character enters the scene. 
However, text assets aren’t intended for text file generation at runtime. For that you need to use input/output programming techniques to read and write external files. For more information on the ways you can generate text in Unity, refer to [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html).
### Binary data
Text assets can also store binary data. If you create a file with the `.bytes` extension, you can load it as a text asset and access it through the `bytes` property.
For example, put a `.jpeg` file into the `Resources` folder and change the extension to `.bytes`, then use the following script code to read the data at runtime:
```
//Load texture from disk
TextAsset bindata = Resources.Load("Texture") as TextAsset;
Texture2D tex = new Texture2D(1,1);
tex.LoadImage(bindata.bytes); 

```

Unity treats files with the `.txt` and `.bytes` extension as text and binary files, respectively. Don’t attempt to store a binary file using the `.txt` extension, because it creates unexpected behavior when attempting to read data from it.
## Additional resources
  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [Supported asset type reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptedImporters.html)
Managing importers with scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html)
Supported asset type reference
