* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.html

# CompilationPipeline
class in UnityEditor.Compilation
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
Methods and properties for script compilation pipeline.
### Static Properties
Property | Description  
---|---  
[codeOptimization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline-codeOptimization.html) | Current code optimization mode.  
### Static Methods
Method | Description  
---|---  
[AssemblyDefinitionReferenceGUIDToGUID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.AssemblyDefinitionReferenceGUIDToGUID.html) | Converts an assembly definition file GUID reference to a GUID string.  
[GetAssemblies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetAssemblies.html) | Get all script assemblies compiled by Unity filtered by AssembliesType.  
[GetAssemblyDefinitionFilePathFromAssemblyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetAssemblyDefinitionFilePathFromAssemblyName.html) | Returns the assembly definition file path from an assembly name. Returns null if there is no assembly definition file for the given assembly name.  
[GetAssemblyDefinitionFilePathFromAssemblyReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetAssemblyDefinitionFilePathFromAssemblyReference.html) | Returns the assembly definition file path for an Assembly Definition File GUID or assembly name reference. Returns null if there is no assembly definition file for the given assembly reference.  
[GetAssemblyDefinitionFilePathFromScriptPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetAssemblyDefinitionFilePathFromScriptPath.html) | Returns the assembly definition file path for a source (script) path. Returns null if there is no assembly definition file for the given script path.  
[GetAssemblyDefinitionPlatforms](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetAssemblyDefinitionPlatforms.html) | Returns all the platforms supported by assembly definition files.Additional resources: AssemblyDefinitionPlatform.  
[GetAssemblyDefinitionReferenceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetAssemblyDefinitionReferenceType.html) | Utility method to determine whether an Assembly Definition File reference is a GUID reference or an assembly name reference.  
[GetAssemblyNameFromScriptPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetAssemblyNameFromScriptPath.html) | Returns the assembly name for a source (script) path. Returns null if there is no assembly name for the given script path.  
[GetAssemblyRootNamespaceFromScriptPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetAssemblyRootNamespaceFromScriptPath.html) | Gets the root namespace associated with the given script path.  
[GetDefinesFromAssemblyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetDefinesFromAssemblyName.html) | Lists all the #define directives used to compile the specified assembly.  
[GetPrecompiledAssemblyNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetPrecompiledAssemblyNames.html) | Get all precompiled assembly names.  
[GetPrecompiledAssemblyPathFromAssemblyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetPrecompiledAssemblyPathFromAssemblyName.html) | Returns the Assembly file path from an assembly name. Returns null if there is no Precompiled Assembly name match.  
[GetPrecompiledAssemblyPaths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetPrecompiledAssemblyPaths.html) | Returns the paths to the precompiled assemblies which are included when building editor assemblies and match any of the given PrecompiledAssemblySources.  
[GetResponseFileDefinesFromAssemblyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetResponseFileDefinesFromAssemblyName.html) | Lists all the #define directives used to compile the specified assembly, that is from a Response File.  
[GetSystemAssemblyDirectories](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetSystemAssemblyDirectories.html) | Use this to get a list of directories containing system references for the specific ApiCompatibilityLevel.  
[GUIDToAssemblyDefinitionReferenceGUID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GUIDToAssemblyDefinitionReferenceGUID.html) | Converts the given GUID to an assembly definition file GUID reference.  
[IsDefineConstraintsCompatible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.IsDefineConstraintsCompatible.html) | Allows you to test whether the specified #define constraints are satisfied by the specified list of #define directives.  
[ParseResponseFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.ParseResponseFile.html) | Retrieves the ResponseFileData describing the content of the response file.  
[RequestScriptCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.RequestScriptCompilation.html) | Allows you to request that the Editor recompile scripts in the project.  
### Events
Event | Description  
---|---  
[assemblyCompilationFinished](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline-assemblyCompilationFinished.html) | An event that is invoked on the main thread when compilation of an assembly finishes.  
[assemblyCompilationNotRequired](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline-assemblyCompilationNotRequired.html) | An event that is invoked on the main thread when an assembly does not require compilation.  
[assemblyCompilationStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline-assemblyCompilationStarted.html) | An event that is invoked on the main thread when the assembly build starts.  
[codeOptimizationChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline-codeOptimizationChanged.html) | This event triggers whenever the codeOptimization property changes between Debug and Release modes.  
[compilationFinished](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline-compilationFinished.html) | An event that is invoked on the main thread when the compilation of assemblies finishes.  
[compilationStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline-compilationStarted.html) | An event that is invoked on the main thread when the compilation of assemblies starts.  
* * *
