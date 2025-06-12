* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * [Organizing scripts into assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)
  * Assembly Definition File Format reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html)
Assembly Definition Reference properties reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping.html)
Managed code stripping
# Assembly Definition File Format reference
Assembly Definition and Assembly Definition Reference assets are JSON files. You can edit the asset files inside the Unity Editor using the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, but you can also modify the JSON content with an external tool.
## Assembly Definition JSON
An Assembly Definition is a JSON object with the following fields:
#### allowUnsafeCode bool
Optional. Defaults to false. See [Allow ‘unsafe’ Code](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#general).
```
"allowUnsafeCode" : true

```

#### autoReferenced bool
Optional. Defaults to true. See [Auto Referenced](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#general).
```
"autoReferenced": false

```

#### defineConstraints string[]
Optional. The symbols that serve as constraints. Can be empty. See [Define Constraints](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#define-constraints).
```
"defineConstraints": [
        "UNITY_2019",
        "UNITY_INCLUDE_TESTS"
    ]

```

#### excludePlatforms string[]
Optional. The platform name strings to exclude or an empty array. The excludePlatforms array must be empty if [includePlatforms](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html#include-platforms) contains values. You can retrieve the platform name strings with the [CompilationPipeline.GetAssemblyDefinitionPlatforms](ScriptRef:CompilationPipeline.GetAssemblyDefinitionPlatforms.html) function (support for a platform must be installed for the current Editor when calling this function.) See [Platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#platforms).
```
"includePlatforms": [],
"excludePlatforms": [
        "iOS",
        "macOSStandalone",
        "tvOS"
]

```

#### includePlatforms string[]
Optional. The platform name strings to include or an empty array. The includePlatforms array must be empty if [excludePlatforms](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html#exclude-platforms) contains values. You can retrieve the platform name strings with the [CompilationPipeline.GetAssemblyDefinitionPlatforms](ScriptRef:CompilationPipeline.GetAssemblyDefinitionPlatforms.html) function (support for a platform must be installed for the current Editor when calling this function.) See [Platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#platforms).
```
"includePlatforms": [
        "Android",
        "LinuxStandalone64",
        "WebGL"
],
"excludePlatforms": []

```

#### name string
Required. Any [legal assembly name](https://docs.microsoft.com/en-us/dotnet/standard/assembly/names).
```
"name" : "MyAssemblyName" 

```

#### noEngineReferences bool
Optional. Defaults to false. See [No Engine References](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#general). 
```
"noEngineReferences": false

```

#### optionalUnityReferences string[]
Optional. In earlier versions of Unity, this field serialized the **Unity References : Test Assemblies** option used to designate the assembly as a test assembly. As of Unity 2019.3, the option is no longer displayed. The field is still supported, but if the asset is reserialized in a newer version of the Unity Editor, the field is replaced by the equivalent assembly references.
See [Creating a test assembly](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html#create-test-assembly) for more information about test assemblies.
```
"optionalUnityReferences": [
    "TestAssemblies"
  ]

```

#### overrideReferences bool
Optional. Set to true if [precompiledReferences](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html#precompiled-references) contains values. Defaults to false. 
See [Override References].
```
"overrideReferences": true

```

#### precompiledReferences string[]
Optional. The file names of referenced DLL libraries including extension, but without other path elements. Can be empty. This array is ignored unless you set [overrideReferences](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-file-format.html#override-references) to true. 
See [Assembly References](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#assembly-references).
```
"overrideReferences": true,
"precompiledReferences": [
        "Newtonsoft.Json.dll",
        "nunit.framework.dll"
]

```

#### references string[]
Optional. References to other assemblies created with Assembly Definition assets. You can use either the GUID of the Assembly Definition asset file or the name of the assembly (as defined by the [name](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#name) field of the Assembly Definition). You must use the same form for all references in the list. Can be empty.
You can use the [AssetDatabase.AssetPathToGUID](ScriptRef:AssetDatabase.AssetPathToGUID.html) function to retrieve the GUID of an asset. (The GUID is also part of the metadata associated with every asset.)
Note that the Editor displays a **Use GUIDs** option in the Assembly Definition Inspector. This option is not serialized in the associated JSON file. Instead, the choice is inferred from the form of reference found in the file.
See [Referencing another assembly](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html#reference-another-assembly).
Using GUIDs:
```
"references": [
        "GUID:17b36165d09634a48bf5a0e4bb27f4bd",
        "GUID:b470eee7144904e59a1064b70fa1b086",
        "GUID:2bafac87e7f4b9b418d9448d219b01ab",
        "GUID:27619889b8ba8c24980f49ee34dbb44a",
        "GUID:0acc523941302664db1f4e527237feb3"
]

```

Using assembly names:
```
"references": [
        "Unity.CollabProxy.Editor",
        "AssemblyB",
        "UnityEngine.UI",
        "UnityEngine.TestRunner",
        "UnityEditor.TestRunner"
]

```

#### versionDefines object[]
Optional. Contains an object for each version define. This object has three fields:
  * name:string – the name of the resource
  * expression:string – the expression defining the version or range of versions of the resource
  * define:string – the symbol to define


See [Version Defines](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html#version-defines).
```
"versionDefines": [
    {
        "name": "com.unity.ide.vscode",
        "expression": "[1.7,2.4.1]",
        "define": "MY_SYMBOL"
    },
    {
        "name": "com.unity.test-framework",
        "expression": "[2.7.2-preview.8]",
        "define": "TESTS"
    }
]

```

### Example Assembly Definition JSON strings
Using assembly names for references to other Assembly Definitions and _includePlatforms_ :
```
{
    "name": "BeeAssembly",
    "references": [
        "Unity.CollabProxy.Editor",
        "AssemblyB",
        "UnityEngine.UI",
        "UnityEngine.TestRunner",
        "UnityEditor.TestRunner"
    ],
    "includePlatforms": [
        "Android",
        "LinuxStandalone64",
        "WebGL"
    ],
    "excludePlatforms": [],
    "overrideReferences": true,
    "precompiledReferences": [
        "Newtonsoft.Json.dll",
        "nunit.framework.dll"
    ],
    "autoReferenced": false,
    "defineConstraints": [
        "UNITY_2019",
        "UNITY_INCLUDE_TESTS"
    ],
    "versionDefines": [
        {
            "name": "com.unity.ide.vscode",
            "expression": "[1.7,2.4.1]",
            "define": "MY_SYMBOL"
        },
        {
            "name": "com.unity.test-framework",
            "expression": "[2.7.2-preview.8]",
            "define": "TESTS"
        }
    ],
    "noEngineReferences": false
}

```

Using GUIDS for references to other Assembly Definitions and _excludePlatforms_ :
```
{
    "name": "BeeAssembly",
    "references": [
        "GUID:17b36165d09634a48bf5a0e4bb27f4bd",
        "GUID:b470eee7144904e59a1064b70fa1b086",
        "GUID:2bafac87e7f4b9b418d9448d219b01ab",
        "GUID:27619889b8ba8c24980f49ee34dbb44a",
        "GUID:0acc523941302664db1f4e527237feb3"
    ],
    "includePlatforms": [],
    "excludePlatforms": [
        "iOS",
        "macOSStandalone",
        "tvOS"
    ],
    "allowUnsafeCode": false,
    "overrideReferences": true,
    "precompiledReferences": [
        "Newtonsoft.Json.dll",
        "nunit.framework.dll"
    ],
    "autoReferenced": false,
    "defineConstraints": [
        "UNITY_2019",
        "UNITY_INCLUDE_TESTS"
    ],
    "versionDefines": [
        {
            "name": "com.unity.ide.vscode",
            "expression": "[1.7,2.4.1]",
            "define": "MY_SYMBOL"
        },
        {
            "name": "com.unity.test-framework",
            "expression": "[2.7.2-preview.8]",
            "define": "TESTS"
        }
    ],
    "noEngineReferences": false
}

```

## Assembly Definition Reference JSON
An Assembly Definition Reference is a JSON object with the following field:
#### reference string
Required. The assembly definition to reference. See [Assembly Definition References](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html).
You can reference an Assembly Definition asset using either the name of the assembly or the GUID of the asset.You can use the [AssetDatabase.AssetPathToGUID](ScriptRef:AssetDatabase.AssetPathToGUID.html) function to retrieve the GUID of an asset. (The GUID is also part of the metadata associated with every asset.)
Using assembly name:
```
{
    "reference": "AssemblyA"
}

```

Using Assembly Definition asset GUID
```
{
    "reference": "GUID:f4de40948f4904ecb94b59dd38aab8a1"
}

```

See [Creating an Assembly Definition Reference asset](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html#create-asmref).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionReferenceImporter.html)
Assembly Definition Reference properties reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping.html)
Managed code stripping
