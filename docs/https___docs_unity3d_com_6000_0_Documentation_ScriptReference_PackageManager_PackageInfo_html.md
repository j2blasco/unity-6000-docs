* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html

# PackageInfo
class in UnityEditor.PackageManager
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
### Description
Structure describing a Unity Package.
Either a reference to a package in a registry, to a revision of a source repository, a resource on the net or to a package available on disk.
### Properties
Property | Description  
---|---  
[assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-assetPath.html) | The asset path of the package in the AssetDatabase.  
[author](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-author.html) | An AuthorInfo instance of the author of the package.  
[category](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-category.html) | Category of the package.  
[changelogUrl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-changelogUrl.html) | The custom URL for the changelog for the package.  
[datePublished](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-datePublished.html) | The date and time at which the package was published.  
[dependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-dependencies.html) | An array of DependencyInfos listing all the packages this package directly depends on.  
[deprecationMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-deprecationMessage.html) | Deprecation message for the version that this instance represents.  
[description](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-description.html) | Detailed description of the package.  
[displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-displayName.html) | Friendly display name of the package.  
[documentationUrl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-documentationUrl.html) | The custom URL for documentation for the package.  
[errors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-errors.html) | The errors associated with the package.  
[git](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-git.html) | A GitInfo instance providing detailed information for a Git package.  
[isDeprecated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-isDeprecated.html) | Set to `true` if the package version that this instance represents is deprecated.  
[isDirectDependency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-isDirectDependency.html) | If the package is a direct dependency of the project.  
[keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-keywords.html) | An array of keywords associated with the package.  
[licensesUrl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-licensesUrl.html) | The custom URL for the licenses of a package.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-name.html) | Unique name of the package.  
[packageId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-packageId.html) | Identifier of the package.  
[registry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-registry.html) | The registry where the Package Manager might find this package.  
[repository](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-repository.html) | A RepositoryInfo instance containing information the repository that the package is hosted on.  
[resolvedDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-resolvedDependencies.html) | An array of DependencyInfo instances listing all the packages this package directly or indirectly depends on and the versions they resolved to.  
[resolvedPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-resolvedPath.html) | The local path of the project on disk.  
[source](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-source.html) | Source of the package contents.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-type.html) | Type of the package.  
[version](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-version.html) | Version of the package.  
[versions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-versions.html) | A VersionsInfo instance containing information about the available versions of the package.  
### Static Methods
Method | Description  
---|---  
[FindForAssembly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.FindForAssembly.html) | Retrieves information about the package containing an assembly, or the assembly definition used to build that assembly.  
[FindForAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.FindForAssetPath.html) | Retrieves information about the package containing an asset based on the path of that asset.  
[FindForPackageName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.FindForPackageName.html) | Retrieves information about the package based on the name of that package.  
[GetAllRegisteredPackages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.GetAllRegisteredPackages.html) | Retrieves information about all packages that are currently loaded.  
[IsPackageRegistered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.IsPackageRegistered.html) | Checks if a specific package is registered with the UnityEditor.AssetDatabase.  
* * *
