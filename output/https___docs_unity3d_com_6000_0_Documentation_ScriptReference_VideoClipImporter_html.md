* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.html

# VideoClipImporter
class in UnityEditor
/
Inherits from:[AssetImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.html)
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
VideoClipImporter lets you modify [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) import settings from Editor scripts.
See the **Movie File Format Support Notes** section in the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) class documentation for supported movie file formats and encoding guidelines. 
### Properties
Property | Description  
---|---  
[defaultTargetSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-defaultTargetSettings.html) | Default values for the platform-specific import settings.  
[deinterlaceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-deinterlaceMode.html) | Images are deinterlaced during transcode. This tells the importer how to interpret fields in the source, if any.  
[flipHorizontal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-flipHorizontal.html) | Apply a horizontal flip during import.  
[flipVertical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-flipVertical.html) | Apply a vertical flip during import.  
[frameCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-frameCount.html) | Number of frames in the clip.  
[frameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-frameRate.html) | Frame rate of the clip.  
[importAudio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-importAudio.html) | Import audio tracks from source file.  
[isPlayingPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-isPlayingPreview.html) | Whether the preview is currently playing.  
[keepAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-keepAlpha.html) | Whether to keep the alpha from the source into the transcoded clip.  
[outputFileSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-outputFileSize.html) | Size in bytes of the file once imported.  
[pixelAspectRatioDenominator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-pixelAspectRatioDenominator.html) | Denominator of the pixel aspect ratio (num:den).  
[pixelAspectRatioNumerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-pixelAspectRatioNumerator.html) | Numerator of the pixel aspect ratio (num:den).  
[sourceAudioTrackCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-sourceAudioTrackCount.html) | Number of audio tracks in the source file.  
[sourceFileSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-sourceFileSize.html) | Size in bytes of the file before importing.  
[sourceHasAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-sourceHasAlpha.html) | True if the source file has a channel for per-pixel transparency.  
[sRGBClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-sRGBClip.html) | Whether the imported clip contains sRGB color data.  
[transcodeSkipped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-transcodeSkipped.html) | Returns true if transcoding was skipped during import, false otherwise. (Read Only)When VideoImporterTargetSettings.enableTranscoding is set to true, the resulting transcoding operation done at import time may be quite long, up to many hours depending on source resolution and content duration. An option to skip this process is offered in the asset import progress bar. When skipped, the transcoding instead provides a non-transcoded verision of the asset. However, the importer settings stay intact so this property can be inspected to detect the incoherence with the generated artifact.Re-importing without stopping the transcode process, or with transcode turned off, causes this property to become false.  
### Public Methods
Method | Description  
---|---  
[ClearTargetSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.ClearTargetSettings.html) | Clear the platform-specific import settings for the specified platform, causing them to go back to the default settings.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.Equals.html) | Performs a value comparison with another VideoClipImporter.  
[GetPreviewTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.GetPreviewTexture.html) | Returns a texture with the transcoded clip's current frame. Returns frame 0 when not playing, and frame at current time when playing.  
[GetResizeHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.GetResizeHeight.html) | Get the resulting height of the resize operation for the specified resize mode.  
[GetResizeModeName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.GetResizeModeName.html) | Get the full name of the resize operation for the specified resize mode.  
[GetResizeWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.GetResizeWidth.html) | Get the resulting width of the resize operation for the specified resize mode.  
[GetSourceAudioChannelCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.GetSourceAudioChannelCount.html) | Number of audio channels in the specified source track.  
[GetSourceAudioSampleRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.GetSourceAudioSampleRate.html) | Sample rate of the specified audio track.  
[GetTargetSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.GetTargetSettings.html) | Returns the platform-specific import settings for the specified platform.  
[PlayPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.PlayPreview.html) | Starts preview playback.  
[SetTargetSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.SetTargetSettings.html) | Sets the platform-specific import settings for the specified platform.  
[StopPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.StopPreview.html) | Stops preview playback.  
### Inherited Members
### Properties
Property | Description  
---|---  
[assetBundleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleName.html) | Get or set the AssetBundle name.  
[assetBundleVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleVariant.html) | Get or set the AssetBundle variant.  
[assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetPath.html) | The path name of the asset for this importer. (Read Only)  
[importSettingsMissing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-importSettingsMissing.html) | The value is true when no meta file is provided with the imported asset.  
[userData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-userData.html) | Get or set any user data.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[AddRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.AddRemap.html) | Map a sub-asset from an imported asset (such as an FBX file) to an external Asset of the same type.  
[GetExternalObjectMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetExternalObjectMap.html) | Gets a copy of the external object map used by the AssetImporter.  
[RemoveRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.RemoveRemap.html) | Removes an item from the map of external objects.  
[SaveAndReimport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SaveAndReimport.html) | Save asset importer settings if asset importer is dirty.  
[SetAssetBundleNameAndVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SetAssetBundleNameAndVariant.html) | Set the AssetBundle name and variant.  
[SupportsRemappedAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SupportsRemappedAssetType.html) | Checks if the AssetImporter supports remapping the given asset type.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[GetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html) | Retrieves the asset importer for the asset at path.  
[GetImportLog](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetImportLog.html) | Retrieves logs generated during the import of the asset at path.  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
