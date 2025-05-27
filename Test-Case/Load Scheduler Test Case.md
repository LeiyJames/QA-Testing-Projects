# 📅 Load Scheduler - Test Cases

## 1. Navbar & General UI
| TC-ID | Description | Steps | Expected Result |
|-------|-------------|-------|-----------------|
| TC-01 | Navbar Navigation | Click `Contact`, `Schedule`, `Transaction` tabs | Correct page loads without errors |

## 2. Contact Module

### ➕ Add Contact
| TC-02 | Add Individual Contact | 1. Click `Add Contact`<br>2. Fill valid details<br>3. Submit | Contact appears in Individual Section |
| TC-03 | Add Invalid Contact | Submit with empty required fields | Shows validation errors |

### 📤 Upload Contact
| TC-04 | Upload Valid CSV | 1. Click `Upload`<br>2. Select valid CSV<br>3. Submit | "X contacts imported successfully" |
| TC-05 | Upload Invalid CSV | Upload file with wrong format | "Invalid file format" error |

### 👤 Individual/Group Sections
| TC-06 | View Individual Contacts | Navigate to Individual Section | Lists all contacts with details |
| TC-07 | View Group Contacts | Navigate to Group Section | Shows grouped contacts properly |

### 🔍 Side Features
| TC-08 | Search Functionality | Type name in search bar | Filters contacts in real-time |
| TC-09 | Filter Options | Apply multiple filters | Shows accurate filtered results |
| TC-10 | Print Feature | Click print button | Generates PDF/printable view |

## 3. Schedule Module

### 📊 Projection Dashboard
| TC-11 | View Today's Schedule | Click "Today" tab | Shows only today's schedules |
| TC-12 | View Weekly Schedule | Click "Week" tab | Groups schedules by day |

### ⏱️ Schedule Management
| TC-13 | Pause Schedule | Click pause icon on active schedule | Status changes to "Paused" |
| TC-14 | Delete Schedule | Click delete and confirm | Schedule removed from list |

### 📋 Detail View
| TC-15 | View Schedule Details | Click any schedule | Shows all metadata correctly |

## 4. Transaction Module

### ⏳ Pending Transactions
| TC-16 | View Pending | Navigate to Pending tab | Lists queued transactions |
| TC-17 | Cancel Transaction | Click cancel button | Moves to "Cancelled" status |

### 📜 History
| TC-18 | Filter History | Use date range filter | Shows transactions in period |

## 5. Edge Cases
| TC-19 | Bulk Upload | Upload 10,000+ contacts | System handles without crashing |
| TC-20 | Special Characters | Use contacts with é,ñ,ü | Displays and searches correctly |

## 🛠️ Test Data Requirements
- Valid CSV template
- Test accounts with different permissions
- Sample schedules with varying frequencies

## 🚦 Priority Matrix
| Priority | Test Cases |
|----------|------------|
| Critical | TC-01, TC-04, TC-13 |
| High     | TC-02, TC-11, TC-16 |
| Medium   | TC-08, TC-15, TC-18 |
| Low      | TC-10, TC-20 |
