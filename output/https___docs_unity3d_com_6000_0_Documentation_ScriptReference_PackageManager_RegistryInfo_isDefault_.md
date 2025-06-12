* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.RegistryInfo-isDefault.html

#  [RegistryInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.RegistryInfo.html).isDefault
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html "Go to PackageManager Component in the Manual")
isDefault; 
### Description
Whether this is the default, Unity registry or one of the scoped registries configured in the project manifest.
The default registry hosts the standard Unity packages. The Package Manager always looks for packages in the default registry unless a project manifest contains one or more scoped registries. When a manifest declares a scoped registry, the Package Manager uses the scope to determine whether to look for a package in that registry. You can configure scoped registries inside a `scopedRegistries` element of your Project manifest file. All configured registries must support the npm protocol.
```
{
    "scopedRegistries": [
        {
            "name": "General",
            "url": "https://example.com/registry",
            "scopes": [ "com.example", "com.example.tools.physics"]
        }
    ],
    "dependencies": {
        "com.unity.animation": "1.0.0",
        "com.example.mycompany.tools.animation": "1.0.0",
        "com.example.animation": "1.0.0"
    }
}
```

* * *
