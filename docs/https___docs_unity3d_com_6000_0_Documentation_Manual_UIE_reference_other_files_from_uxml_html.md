* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-reference-other-files-from-uxml.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Structure UI with UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * Reference other files from UXML


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-reuse-uxml-files.html)
Reuse UXML files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-manage-asset-reference.html)
Load UXML and USS C# scripts
# Reference other files from UXML
In a UXML file, you can use the `<Template>` and the `<Style>` elements to reference other UXML or USS files. The two elements both accept either an `src` attribute or a `path` attribute.
## The `src` attribute
Use the following syntax for the src attribute:
```
src="<path-to-file>/<file-name-with-extension>"

```

Any errors during import, such as missing files, trigger an error message.
You can use a relative or an absolute path: 
  * Absolute paths start from the project’s `Assets` folder and begin with a `/` or `project://database/`. For example, `/Assets/myFolder/myFile.uss` or `project://database/Assets/myFolder/myFile.uss`.
  * Relative paths start from the current file and exclude the `/`. For example, `../myFolder/myFile.uss`.


**Note** : To reference a file from packages, use the absolute path of the package file that starts from the `Packages` folder. For example, `/Packages/com.unity.package.name/file-name.uss` or `project://database/Packages/com.unity.package.name/file-name.uss`. you must use the format of `com.unity.package.name` rather than `package name` for the package name. 
## The `path` attribute
The `path` attribute uses the Unity Resources mechanisms, but doesn’t offer error reporting at import time and doesn’t allow relative paths.
The `path` attribute accepts files located in either the `Resources` folder or the `Editor Default Resources` folder, with the following rules:
  * If the file is in the `Resources` folder, don’t include the file extension. For example, write `path="template"` for a file located at `Assets/Resources/template.uxml`.
  * If the file is in the `Editor Default Resources` folder, you must include the file extension. For example, write `path="template.uxml"` for a file located at `Assets/Editor Default Resources/template.uxml`.


## Additional resources
  * [Add styles to UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-add-style-to-uxml.html)
  * [Reuse UXML files](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-reuse-uxml-files.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-reuse-uxml-files.html)
Reuse UXML files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-manage-asset-reference.html)
Load UXML and USS C# scripts
