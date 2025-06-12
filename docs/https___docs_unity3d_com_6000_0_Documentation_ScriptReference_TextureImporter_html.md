* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html

# TextureImporter
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html "Go to TextureImporter Component in the Manual")
### Description
Texture importer lets you modify [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) import settings from editor scripts.
Settings of this class cover most of the settings exposed in [Texture Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html). Some settings require you to use [TextureImporterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html). Refer to [TextureImporter.SetTextureSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.SetTextureSettings.html)).
### Properties
Property | Description  
---|---  
[allowAlphaSplitting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-allowAlphaSplitting.html) | Allows alpha splitting on relevant platforms for this texture.  
[alphaIsTransparency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-alphaIsTransparency.html) | If the alpha channel of your texture represents transparency, enable this property to dilate the color channels of visible texels into fully transparent areas. This effectively adds padding around transparent areas that prevents filtering artifacts from forming on their edges. Unity does not support this property for HDR textures.This property makes the color data of invisible texels undefined. Disable this property to preserve invisible texels' original color data.  
[alphaSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-alphaSource.html) | Select how the alpha of the imported texture is generated.  
[alphaTestReferenceValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-alphaTestReferenceValue.html) | Returns or assigns the alpha test reference value.  
[androidETC2FallbackOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-androidETC2FallbackOverride.html) | ETC2 texture decompression fallback override on Android devices that don't support ETC2.  
[anisoLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-anisoLevel.html) | Anisotropic filtering level of the texture.  
[borderMipmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-borderMipmap.html) | Keeps texture borders the same when generating mipmaps.  
[compressionQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-compressionQuality.html) | The quality of the texture after Crunch compresses it. The range is 0 through 100. A higher value means a larger, better-quality texture, but a longer compression time because Crunch needs more time to try different texture encodings.  
[convertToNormalmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-convertToNormalmap.html) | Convert heightmap to normal map  
[crunchedCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-crunchedCompression.html) | Use crunched compression when available.  
[fadeout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-fadeout.html) | Fade out mip levels to gray color.  
[filterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-filterMode.html) | Filtering mode of the texture.  
[flipGreenChannel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-flipGreenChannel.html) | Indicates whether to invert the green channel values of a normal map.  
[generateCubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-generateCubemap.html) | Cubemap generation mode.  
[heightmapScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-heightmapScale.html) | Amount of bumpyness in the heightmap.  
[ignoreMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-ignoreMipmapLimit.html) | Enable this flag for textures that should ignore mipmap limit settings.  
[ignorePngGamma](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-ignorePngGamma.html) | Ignore the Gamma attribute in PNG files. This property does not effect other file formats.  
[isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-isReadable.html) | Whether Unity stores an additional copy of the imported texture's pixel data in CPU-addressable memory.  
[maxTextureSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-maxTextureSize.html) | Maximum texture size.  
[mipMapBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-mipMapBias.html) | Mip map bias of the texture.  
[mipmapEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-mipmapEnabled.html) | Generate Mip Maps.  
[mipmapFadeDistanceEnd](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-mipmapFadeDistanceEnd.html) | Mip level where texture is faded out completely.  
[mipmapFadeDistanceStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-mipmapFadeDistanceStart.html) | Mip level where texture begins to fade out.  
[mipmapFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-mipmapFilter.html) | Mipmap filtering mode.  
[mipmapLimitGroupName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-mipmapLimitGroupName.html) | Name of the texture mipmap limit group to which this texture belongs.  
[mipMapsPreserveCoverage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-mipMapsPreserveCoverage.html) | Enables or disables coverage-preserving alpha mipmapping.  
[normalmapFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-normalmapFilter.html) | Normal map filtering mode.  
[npotScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-npotScale.html) | Scaling mode for non power of two textures.  
[qualifiesForSpritePacking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-qualifiesForSpritePacking.html) | Returns true if this TextureImporter is setup for Sprite packing.  
[secondarySpriteTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-secondarySpriteTextures.html) | Secondary textures for the imported Sprites.  
[spriteBorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-spriteBorder.html) | Border sizes of the generated sprites.  
[spriteImportMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-spriteImportMode.html) | Selects Single or Manual import mode for Sprite textures.  
[spritePivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-spritePivot.html) | The point in the Sprite object's coordinate space where the graphic is located.  
[spritePixelsPerUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-spritePixelsPerUnit.html) | The number of pixels in the sprite that correspond to one unit in world space.  
[sRGBTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-sRGBTexture.html) | Whether this texture stores data in sRGB (also called gamma) color space.  
[streamingMipmaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-streamingMipmaps.html) | Enable mipmap streaming for this texture.  
[streamingMipmapsPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-streamingMipmapsPriority.html) | Relative priority for this texture when reducing memory size in order to hit the memory budget.  
[swizzleA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-swizzleA.html) | Specifies the source for the texture's alpha color channel data.  
[swizzleB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-swizzleB.html) | Specifies the source for the texture's blue color channel data.  
[swizzleG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-swizzleG.html) | Specifies the source for the texture's green color channel data.  
[swizzleR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-swizzleR.html) | Specifies the source for the texture's red color channel data.  
[textureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-textureCompression.html) | Compression of imported texture.  
[textureShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-textureShape.html) | The shape of the imported texture.  
[textureType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-textureType.html) | Which type of texture are we dealing with here.  
[vtOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-vtOnly.html) | When enabled, this texture can solely be used in combination with a Texture Stack for Virtual Texturing. When enabled the texture is not guaranteed to be available as a Texture2D in the Player (e.g., not accessible from a script). When disabled, the Player includes the texture both as a Texture2D (e.g., accessible from script) and as a streamable texture in a Texture Stack.  
[wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-wrapMode.html) | Texture coordinate wrapping mode.  
[wrapModeU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-wrapModeU.html) | Texture U coordinate wrapping mode.  
[wrapModeV](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-wrapModeV.html) | Texture V coordinate wrapping mode.  
[wrapModeW](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-wrapModeW.html) | Texture W coordinate wrapping mode for Texture3D.  
### Public Methods
Method | Description  
---|---  
[ClearPlatformTextureSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.ClearPlatformTextureSettings.html) | Clears specific target platform settings.  
[DoesSourceTextureHaveAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.DoesSourceTextureHaveAlpha.html) | Allows you to check whether the texture source image has an alpha channel.  
[GetAutomaticFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.GetAutomaticFormat.html) | Returns the TextureImporterFormat that would be automatically chosen for this platform.  
[GetDefaultPlatformTextureSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.GetDefaultPlatformTextureSettings.html) | Gets the default platform specific texture settings.  
[GetPlatformTextureSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.GetPlatformTextureSettings.html) | Gets platform specific texture settings.  
[GetSourceTextureWidthAndHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.GetSourceTextureWidthAndHeight.html) | Gets the source texture's width and height.  
[ReadTextureImportInstructions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.ReadTextureImportInstructions.html) | Reads the active texture output instructions of this TextureImporter.  
[ReadTextureSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.ReadTextureSettings.html) | Read texture settings into TextureImporterSettings class.  
[SetPlatformTextureSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.SetPlatformTextureSettings.html) | Sets specific target platform settings.  
[SetTextureSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.SetTextureSettings.html) | Sets texture importers settings from TextureImporterSettings class.  
### Static Methods
Method | Description  
---|---  
[IsDefaultPlatformTextureFormatValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.IsDefaultPlatformTextureFormatValid.html) | Validates TextureImporterFormat based on the type of the current format (TextureImporterType) and the default platform.  
[IsPlatformTextureFormatValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.IsPlatformTextureFormatValid.html) | Validates TextureImporterFormat based on a specified import type (TextureImporterType) and a specified build target (BuildTarget.).  
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
