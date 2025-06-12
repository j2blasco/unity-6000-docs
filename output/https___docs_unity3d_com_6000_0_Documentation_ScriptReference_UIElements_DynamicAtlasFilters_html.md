* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasFilters.html

# DynamicAtlasFilters
enumeration
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
Options to enable or disable filters for the dynamic atlas. 
Filters exclude individual textures from the texture atlas based on specific criteria. 
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasFilters.None.html) |  No filtering is performed.   
[Readability](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasFilters.Readability.html) |  Excludes readable textures. Readable textures are textures that are readable from scripts, which means they are also writable or editable. Another way to think of this filter is as a way to exclude textures that are not read-only.   
[Size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasFilters.Size.html) |  Excludes textures whose size exceeds the maximum sub-texture size specified in the dynamic atlas settings.   
[Format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasFilters.Format.html) |  Excludes textures that, because of their format, would lose precision, or be truncated when the system adds them to the atlas. The dynamic atlas system accepts non-HDR texture formats that have 8 bits or less per component, before compression You can add a compressed texture to a dynamic atlas. However, doing so might cause additional image loss because the system must first decompress the image in order to store it in the atlas. Decompression can yield values that are impossible to represent precisely in 8-bits per component. For example, a value of 1/256 in the compressed image might decompress to 3/512. The system cannot store 3/512 in the atlas, so it stores the value as either 1/256 or 2/256. This creates potential differences between the source texture and the version stored in the atlas. These differences are noticeable in the following scenarios: 1. Blending Operations: 3/512, 1/256, and 2/256 each produce a different result when you use them in a blending operation. 2. Rendering to high precision render targets (for example, 16 bits per component). In most cases, the performance benefits of allowing compressed textures into the atlas outweigh the inconvenience of introducing small errors.   
[ColorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasFilters.ColorSpace.html) |  Excludes textures whose color space does not match the color space of the atlas.   
[FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasFilters.FilterMode.html) |  Excludes textures that use a filter mode that the atlas does not support. This filter is disabled by default. You can enable it to prevent artifacts that might occur when the atlas does not support the texture's filter mode, and cannot sample the texture correctly. However, because excluding textures from the atlas can reduce performance, the default behavior is preferable in most cases. On GLES3 (and later) devices, the atlas supports more than one filter mode, so you should not need to enable this filter.   
* * *
