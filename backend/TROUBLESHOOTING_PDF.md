# Troubleshooting PDF Indexing Issues

## Problem
PDF documents are not showing up as sources in query results, even though they are in the data folder.

## Common Causes

### 1. **Stale Index**
The most common cause is that the FAISS index was created before PDFs were added or when PDF loading was failing.

**Solution:** Re-index all documents:
```bash
curl -X POST http://localhost:8000/reindex
```

### 2. **PDF Loading Failures**
PDFs may fail to load due to:
- **Corrupted files**: Especially common with Chrome-saved PDFs
- **Password-protected PDFs**: Cannot be loaded without password
- **Image-only PDFs**: PDFs that are scanned images without text layer
- **Unusual encoding**: Some PDFs have non-standard encoding

**Check the logs:**
When you start the server or call `/reindex`, look for error messages:
```
[TIMESTAMP] ERROR: Failed to load PDF /path/to/file.pdf: <error details>
```

### 3. **Missing Dependencies**
Ensure all required packages are installed:
```bash
pip install -r requirements.txt
```

## Diagnostic Steps

### Step 1: Check Current Stats
Call the stats endpoint to see what's in your data folder:
```bash
curl http://localhost:8000/stats
```

Look for the `files_by_type` field to see the breakdown.

### Step 2: Re-index with Diagnostics
Stop the server and re-index:
```bash
curl -X POST http://localhost:8000/reindex
```

Watch the console output carefully. You should see:
- "Successfully loaded PDF: filename.pdf (X pages)" for each successful PDF
- "Failed to load PDF: filename.pdf: <error>" for each failed PDF
- A summary at the end showing how many files of each type loaded successfully

### Step 3: Check for Specific Errors
Common error messages and solutions:

#### "Failed to load PDF: ... EOF marker not found"
- The PDF is corrupted or incomplete
- **Solution**: Re-download or re-save the PDF

#### "Failed to load PDF: ... PyCryptodome is required for AES algorithm"
- The PDF is encrypted/password-protected
- **Solution**: Remove password protection or install PyCryptodome

#### "PDF loaded but contains no pages"
- The PDF file is empty or invalid
- **Solution**: Check the PDF manually to ensure it has content

## Chrome PDF Issues

Chrome-saved PDFs can sometimes have issues:

### Problem: Chrome saves web pages as PDFs that don't load properly
**Solutions:**
1. Try saving the page using "Print to PDF" instead of "Save as PDF"
2. Open the Chrome PDF in another PDF viewer and re-save it
3. Use a PDF repair tool to fix the file

### Problem: Chrome PDFs are image-based (no text layer)
**Solution:** The current implementation uses PyPDFLoader which only extracts text. For image-based PDFs, you would need OCR (Optical Character Recognition). This is not currently implemented.

## Advanced Diagnostics

### Check if a specific PDF can be loaded
Create a test script:
```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("path/to/your/file.pdf")
try:
    documents = loader.load()
    print(f"✓ Loaded {len(documents)} pages")
    for i, doc in enumerate(documents):
        print(f"Page {i}: {len(doc.page_content)} characters")
except Exception as e:
    print(f"✗ Failed: {e}")
```

## After Fixing Issues

Once you've identified and fixed the issue:
1. Call `POST /reindex` to rebuild the index
2. Verify in the logs that PDFs loaded successfully
3. Try a test query
4. Check that PDF sources appear in the response

## Still Having Issues?

If PDFs still don't show up after re-indexing:
1. Check that the index was actually rebuilt (look for "Document Loading Summary" in logs)
2. Verify that PDFs have content: `pdftotext yourfile.pdf` should show text
3. Try with a simple test PDF first to rule out file-specific issues
4. Check that you're querying about content that's actually in the PDFs
