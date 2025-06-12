* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprites.Packer.GetAlphaTexturesForAtlas.html

#  [Packer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprites.Packer.html).GetAlphaTexturesForAtlas
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
## Declaration
public static Texture2D[] GetAlphaTexturesForAtlas(string atlasName); 
### Parameters
Parameter | Description  
---|---  
atlasName | Name of the atlas.  
### Description
Returns all alpha atlas textures generated for the specified atlas.
Alpha splits are generated when the textures with alpha are compressed using ETC1 on specific platforms like Android.
* * *
