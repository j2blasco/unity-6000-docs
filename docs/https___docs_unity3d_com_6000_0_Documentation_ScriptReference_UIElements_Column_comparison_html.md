* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-comparison.html

#  [Column](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column.html).comparison
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
comparison; 
### Description
The comparison to use when using [ColumnSortingMode.Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ColumnSortingMode.Default.html). Compares two items by their index in the source. 
The following example creates a [MultiColumnListView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnListView.html) that can be sorted with the default algorithm: 
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.IO;
using System.Text;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;
using Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html) = UnityEngine.Debug;  
  
namespace MultiColumnViewExample
{
    public class FileExplorerWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
    {
        MultiColumnListView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnListView.html) m_ListView;
        List<FileInfoWrapper> m_Source = new List<FileInfoWrapper>();
        StringBuilder m_StringBuilder = new StringBuilder();  
  
        [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MultiColumnView Examples/File[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html) Explorer (List)")]
        public static void ShowExample()
        {
            var wnd = GetWindow<FileExplorerWindow>();
            wnd.titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("File[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html) Explorer");
        }  
  
        public void CreateGUI()
        {
            // Here we're setting up a 3-column list view to display information on all files in the project.
            // Each column will be sorted using the `comparison` callback.
            // Use CTRL/CMD + click on a column header to sort multiple columns.
            // Use Shift + click on a column header to remove sorting.
            m_ListView = new MultiColumnListView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnListView.html)(new Columns[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.html)()
            {
                new Column[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column.html)()
                {
                    name = "filename", title = "Name", minWidth = 600,
                    bindCell = (ve, row) => ((Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html))ve).text = m_Source[row].fullFileName,
                    comparison = (a, b) => m_Source[a].fullFileName.CompareTo(m_Source[b].fullFileName),
                },
                new Column[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column.html)()
                {
                    name = "type", title = "Type", minWidth = 60,
                    bindCell = (ve, row) => ((Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html))ve).text = m_Source[row].type,
                    comparison = (a, b) => m_Source[a].type.CompareTo(m_Source[b].type),
                },
                new Column[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column.html)()
                {
                    name = "size", title = "Size", minWidth = 60,
                    bindCell = (ve, row) => ((Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html))ve).text = m_Source[row].displaySize,
                    comparison = (a, b) => m_Source[a].sizeLong.CompareTo(m_Source[b].sizeLong),
                }
            });  
  
            // This causes the list view to take all the space available.
            m_ListView.style.flexGrow = 1;  
  
            // Setting the sortingMode to Default enables Unity's sorting algorithm, which will use the Columns[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.html)' comparison callbacks.
            m_ListView.sortingMode = ColumnSortingMode.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ColumnSortingMode.Default.html);  
  
            // Use all the files in the project as the source.
            foreach (var file in Directory.EnumerateFiles(Application.dataPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html), "*.*", SearchOption.AllDirectories))
            {
                m_Source.Add(new FileInfoWrapper(new FileInfo(file)));
            }  
  
            m_ListView.itemsSource = m_Source;  
  
            // The columnSortingChanged and sortedColumns property can be used to know when the ordering changes.
            // This is the callback to use if you want to implement a custom sorting algorithm, when using ColumnSortingMode.Custom[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ColumnSortingMode.Custom.html).
            m_ListView.columnSortingChanged += () =>
            {
                m_StringBuilder.Clear();
                foreach (var s in m_ListView.sortedColumns)
                {
                    m_StringBuilder.Append($"Sorted {s.columnName} in {s.direction} order.");
                }  
  
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(m_StringBuilder.ToString());
            };  
  
            rootVisualElement.Add(m_ListView);
        }
    }  
  
    public class FileInfoWrapper
    {
        static readonly string[] k_SizeSuffixes = { "B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB" };  
  
        static string GetBytesReadable(long fileSizeInBytes)
        {
            if (fileSizeInBytes == 0)
                return "0" + k_SizeSuffixes[0];  
  
            var magnitude = (int)Math.Log(fileSizeInBytes, 1024);
            var adjustedSize = fileSizeInBytes / (1L << (magnitude * 10));  
  
            return $"{adjustedSize:n1} {k_SizeSuffixes[magnitude]}";
        }  
  
        public FileInfoWrapper(FileInfo fileInfo)
        {
            fullFileName = fileInfo.FullName;
            type = fileInfo.Extension.Substring(1).ToUpper();
            displaySize = GetBytesReadable(fileInfo.Length);
            sizeLong = fileInfo.Length;
        }  
  
        public readonly string fullFileName;
        public readonly string type;
        public readonly string displaySize;
        public readonly long sizeLong; // It is faster to compare long than strings.
    }
}

```

* * *
