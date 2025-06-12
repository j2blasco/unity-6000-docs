* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.html

# Dependencies
class in Unity.Android.Gradle
/
Inherits from:[Unity.Android.Gradle.BaseBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
The C# definition of the `dependencies` element in a gradle file.
For more information about the element, see Android's documentation: [dependencies](https://developer.android.com/studio/build/dependencies)
### Constructors
Constructor | Description  
---|---  
[Dependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies-ctor.html) | Element constructor.  
### Public Methods
Method | Description  
---|---  
[AddDependencyClasspathByName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.AddDependencyClasspathByName.html) | Adds a depenency by classpath name.  
[AddDependencyImplementationByName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.AddDependencyImplementationByName.html) | Adds a plugin implementation element with name: "implementation '{name}'".  
[AddDependencyImplementationFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.AddDependencyImplementationFiles.html) | Adds a plugin implementation element with files: "implementation files({files})".  
[AddDependencyImplementationFileTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.AddDependencyImplementationFileTree.html) | Adds a plugin implementation element with fileTree: "implementation fileTree(':{name}')".  
[AddDependencyImplementationGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.AddDependencyImplementationGroup.html) | Adds a plugin implementation element as group: "implementation group: '{namespace}', name: '{name}', version: '{version}'".  
[AddDependencyImplementationProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.AddDependencyImplementationProject.html) | Adds a plugin implementation element with project: "implementation project(':{name}')".  
[AddDependencyImplementationRaw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.AddDependencyImplementationRaw.html) | Adds a plugin implementation element with raw value: "implementation {value}".  
[AddDependencyPlugin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.AddDependencyPlugin.html) | Adds a plugin as a dependency.  
### Inherited Members
### Public Methods
Method | Description  
---|---  
[AddElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.AddElement.html) | Adds a new element as a child.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.Clear.html) | Clears the content of this element.  
[GetElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.GetElement.html) | Gets an element by ID.  
[GetElements](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.GetElements.html) | Gets all custom child elements.  
[GetName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.GetName.html) | Gets the name of the block. In some cases, the name is the signature of the function.  
[GetRaw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.GetRaw.html) | Gets the raw value of this block.  
[GetUniqueName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.GetUniqueName.html) | Gets the unique name of the element.  
[RemoveElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.RemoveElement.html) | Removes a child element by id.  
[SetRaw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.SetRaw.html) | Sets a raw string value to this block.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.ToString.html) | Gets a serialized value from this block.  
[AddElementDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.AddElementDependencies.html) | Adds a list of dependencies by ID to this element.  
[AddElementDependency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.AddElementDependency.html) | Adds a dependency to this element.  
[GetElementDependenciesIDs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.GetElementDependenciesIDs.html) | Gets a read-only list of element IDs that this element depends on.  
[GetID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.GetID.html) | Gets the unique ID of this element.  
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.Remove.html) | Removes this element from the file.  
[RemoveAllElementDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.RemoveAllElementDependencies.html) | Remove all element dependencies.  
[RemoveElementDependency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.RemoveElementDependency.html) | Remove an element dependency.  
[RemoveElementDependencyById](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.RemoveElementDependencyById.html) | Remove an element dependency by ID.  
[ResolveConflict](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.ResolveConflict.html) | Resolve a conflict if another script has already modified the element.  
* * *
