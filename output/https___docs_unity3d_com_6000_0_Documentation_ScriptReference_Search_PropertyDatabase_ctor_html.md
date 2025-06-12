* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase-ctor.html

# PropertyDatabase Constructor
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
public PropertyDatabase(string filePath); 
### Parameters
Parameter | Description  
---|---  
filePath | Path to the backing file.  
### Description
Constructs a new instance of a [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).
If **filePath** does not exist, the file will be created automatically. The [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) will not update the backing file automatically, you will have to trigger the update manually with [PropertyDatabase.TriggerBackgroundUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.TriggerBackgroundUpdate.html). If another [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) is already opened on the same file, the [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) will not be opened and will be invalid. See [valid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase-valid.html).
* * *
## Declaration
public PropertyDatabase(string filePath, bool autoFlush, double backgroundUpdateDebounceInSeconds); 
### Parameters
Parameter | Description  
---|---  
filePath | Path to the backing file.  
autoFlush | Boolean indicating if the backing file will be updated automatically or not.  
backgroundUpdateDebounceInSeconds | Time between changes for the automatic background update to trigger.  
### Description
Constructs a new instance of a [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).
If **filePath** does not exist, the file will be created automatically. If **autoBackgroundUpdate** is true, the [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) will automatically update the backing file after changes have completed. To prevent updating the file too often when there is a lot of changes, you can specify a delay between changes with **backgroundUpdateDebounceInSeconds** before the update can trigger. For example, with the default value of 5 seconds, a background update will only happen after 5 seconds have passed since the last changes to the [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html). If another [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) is already opened on the same file, the [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) will not be opened and will be invalid. See [valid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase-valid.html).
* * *
