* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.Update.html

#  [Tile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html).Update
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
public void Update(string xml); 
## Declaration
public void Update(string medium, string wide, string large, string text); 
### Parameters
Parameter | Description  
---|---  
xml | A string containing XML document for new tile look.  
medium | An `uri` to 150x150 image, shown on medium tile.  
wide | An `uri` to a 310x150 image to be shown on a wide tile (if such issupported).  
large | An `uri` to a 310x310 image to be shown on a large tile (if such is supported).  
text | A text to shown on a tile.  
### Description
Send a notification for tile (update tiles look).
A tile is updated by providing and XML document with new look. The second version is a convenience method to make tile display image, text or both. At least one of medium and text argumets must be provided, and these two are used to determine whether this is image-only, text-only or image-and-text tile. Uris ms-appx:/// and ms-appdata://`local` can be used to access local application resources. If uri points to network resource, internet access capability must be enabled in applications manifest.
* * *
