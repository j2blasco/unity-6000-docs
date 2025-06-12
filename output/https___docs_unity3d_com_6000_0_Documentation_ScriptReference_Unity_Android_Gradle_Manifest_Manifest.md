* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.html

# Manifest
class in Unity.Android.Gradle.Manifest
/
Inherits from:[Unity.Android.Gradle.Manifest.BaseElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.html)
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
The C# definition of the ` <manifest> ` Android Manifest element.
For more information about the element, see Android's documentation: [Manifest element](https://developer.android.com/guide/topics/manifest/manifest-element)
### Properties
Property | Description  
---|---  
[Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.Application.html) | Child element <application>.  
[Attributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.Attributes.html) | The attributes container for the <manifest> element.  
[CompatibleScreens](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.CompatibleScreens.html) | Child element <compatible-screens>.  
[InstrumentationList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.InstrumentationList.html) | List of <instrumentation> child elements.  
[PermissionGroupList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.PermissionGroupList.html) | List of <permission-group> child elements.  
[PermissionList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.PermissionList.html) | List of <permission> child elements.  
[PermissionTreeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.PermissionTreeList.html) | List of <permission-tree> child elements.  
[QueriesList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.QueriesList.html) | List of <queries> child elements.  
[SupportsGlTextureList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.SupportsGlTextureList.html) | List of <supports-gl-texture> child elements.  
[SupportsScreens](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.SupportsScreens.html) | Child element <supports-screens>.  
[UsesConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.UsesConfiguration.html) | Child element <uses-configuration>.  
[UsesFeatureList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.UsesFeatureList.html) | List of <uses-feature> child elements.  
[UsesPermissionList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.UsesPermissionList.html) | List of <uses-permission> child elements.  
[UsesPermissionSdk23List](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.UsesPermissionSdk23List.html) | List of <uses-permission-sdk-23> child elements.  
[UsesSdk](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.UsesSdk.html) | Child element <uses-sdk>.  
### Constructors
Constructor | Description  
---|---  
[Manifest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest-ctor.html) | Element constructor.  
### Public Methods
Method | Description  
---|---  
[AddUsesFeature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.AddUsesFeature.html) | Adds <uses-feature> element as a child.  
[AddUsesPermission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.AddUsesPermission.html) | Adds <uses-permission> element as a child.  
[GetActivitiesWithLauncherIntent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Manifest.GetActivitiesWithLauncherIntent.html) | Gets the <activity> elements that contain the LAUNCHER category in an <intent-filter> element.  
### Inherited Members
### Properties
Property | Description  
---|---  
[CustomElements](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.CustomElements.html) | Custom child elements.  
### Public Methods
Method | Description  
---|---  
[AddCustomElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.AddCustomElement.html) | Adds a new element as a child.  
[GetAllAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.GetAllAttributes.html) | Gets all attributes on this element.  
[GetCustomAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.GetCustomAttribute.html) | Gets a custom attribute by attribute name.  
[GetID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.GetID.html) | Gets the unique ID of the element.  
[GetName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.GetName.html) | Gets the element name.  
[GetUniqueName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.GetUniqueName.html) | Gets a unique name of the element.  
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.Remove.html) | Removes this element from the file.  
[RemoveCustomAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.RemoveCustomAttribute.html) | Removes a custom attribute by name.  
[ResolveConflict](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.ResolveConflict.html) | Resolve a conflict if element was already modified by another script.  
[SetCustomAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.BaseElement.SetCustomAttribute.html) | Sets a custom attribute with name and value.  
* * *
