* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasSettings.html

# DynamicAtlasSettings
class in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
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
Contains the settings used by the dynamic atlas system. 
### Static Properties
Property | Description  
---|---  
[defaultFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasSettings-defaultFilters.html) |  Default filters for a dynamic atlas.   
[defaults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasSettings-defaults.html) |  Specifies default values used to initialize the structure.   
### Properties
Property | Description  
---|---  
[activeFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasSettings-activeFilters.html) |  Defines the filters that the dynamic atlas system uses to exclude textures from the texture atlas.   
[customFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasSettings-customFilter.html) |  When a delegate is assigned, the dynamic atlas system calls it to determine whether or not a texture can be added to the atlas.   
[maxAtlasSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasSettings-maxAtlasSize.html) |  Specifies the maximum size (width/height) of the atlas texture, in pixels. This value must be a power of two, and must be greater than or equal to minAtlasSize.   
[maxSubTextureSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasSettings-maxSubTextureSize.html) |  Specifies the maximum size (width/height) of a texture that can be added to the atlas. When activeFilters contains DynamicAtlasFilters.Size, textures larger than this size are excluded from the atlas. Otherwise, this value is not used.   
[minAtlasSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasSettings-minAtlasSize.html) |  Specifies the minimum size (width/height) of the atlas texture, in pixels. This value must be a power of two, and must be greater than 0 and less than or equal to maxAtlasSize.   
* * *
