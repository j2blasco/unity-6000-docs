* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.GetManagedReferencesWithMissingTypes.html

#  [SerializationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.html).GetManagedReferencesWithMissingTypes
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
public static ManagedReferenceMissingType[] GetManagedReferencesWithMissingTypes([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
### Description
Returns the list of managed references that could not be deserialized because of a missing type.
This method returns the list of Managed References objects that could not be deserialized because their type is missing. This information can be used to help resolve missing type occurrences.  
  
Additional resources: [HasManagedReferencesWithMissingTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.HasManagedReferencesWithMissingTypes.html), [ManagedReferenceMissingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedReferenceMissingType.html). 
```
using System.Collections.Generic;
using System.Text;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class GetManagedReferencesWithMissingTypesExample
{
    enum ReportFormat { Detailed, ClassList }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Report MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) Missing SerializeReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) Types")]
    static public void ReportMissingTypes()
    {
        ReportMissingTypesOnActiveMonoBehaviours(ReportFormat.ClassList);
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Report MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) Missing SerializeReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) Types - Detailed")]
    static public void ReportMissingTypesDetailed()
    {
        ReportMissingTypesOnActiveMonoBehaviours(ReportFormat.Detailed);
    }  
  
    static private void ReportMissingTypesOnActiveMonoBehaviours(ReportFormat reportType)
    {
        var report = new StringBuilder();  
  
        // Visit all the active MonoBehaviours
        var myMonoComponents = Object.FindObjectsOfType<MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)>();
        foreach (var monoBehaviour in myMonoComponents)
        {
            ReportReferencesWithMissingTypesOnHost(monoBehaviour, ref report, reportType);
        }  
  
        if (report.Length == 0)
            report.Append("No missing types found");  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(report.ToString());
    }  
  
    static private void ReportReferencesWithMissingTypesOnHost(Object host, ref StringBuilder report, ReportFormat reportType)
    {
        // Report the references that have missing types on an individual MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html), ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) or other host
        if (!SerializationUtility.HasManagedReferencesWithMissingTypes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.HasManagedReferencesWithMissingTypes.html)(host))
            return;  
  
        var missingTypes = SerializationUtility.GetManagedReferencesWithMissingTypes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.GetManagedReferencesWithMissingTypes.html)(host);  
  
        report.Append(reportType == ReportFormat.Detailed ? "Missing references on " : "Missing classes on ");
        MonoBehaviourDescription(host, ref report);  
  
        if (reportType == ReportFormat.Detailed)
        {
            foreach (var missingType in missingTypes)
            {
                report.Append("\t").AppendFormat("{0} - {1}", missingType.referenceId, MissingClassFullName(missingType));
                if (missingType.serializedData.Length > 0)
                    report.Append("\t").AppendFormat("\n\t\t{0}", missingType.serializedData);
                report.AppendLine();
            }
        }
        else
        {
            // Only report each unique class that is missing, rather than all objects using that class
            var missingClasses = new HashSet<string>();
            foreach (var missingType in missingTypes)
            {
                missingClasses.Add(MissingClassFullName(missingType));
            }  
  
            foreach (var missingClass in missingClasses)
            {
                report.Append("\t").Append(missingClass).AppendLine();
            }
        }
    }  
  
    static private void MonoBehaviourDescription(Object host, ref StringBuilder stringBuilder)
    {
        // Identify the object that has missing types
        stringBuilder.AppendFormat("MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) \"{0}\" (Type: {1}, Instance: {2})",
            host.name,
            host.GetType().FullName,
            host.GetInstanceID()).AppendLine();
    }  
  
    static private string MissingClassFullName(ManagedReferenceMissingType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedReferenceMissingType.html) missingType)
    {
        var description = new StringBuilder();
        if (missingType.namespaceName.Length > 0)
            description.Append(missingType.namespaceName).Append(".");
        description.AppendFormat("{0}, {1}", missingType.className, missingType.assemblyName);
        return description.ToString();
    }
}

```

* * *
