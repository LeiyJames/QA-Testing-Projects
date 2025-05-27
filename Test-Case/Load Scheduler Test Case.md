# Load Scheduler Test Cases

## 1. Navbar & General UI
| TC-ID | Description              | Steps                                      | Expected Result                     |
|-------|--------------------------|--------------------------------------------|-------------------------------------|
| TC-01 | Navbar Navigation        | Click `Contact`, `Schedule`, `Transaction` | Correct page loads without errors   |

## 2. Contact Module

### 2.1 Add Contact
| TC-02 | Add Individual Contact | 1. Click `Add Contact`<br>2. Fill details<br>3. Submit | Contact saved; appears in Individual Section |
| TC-03 | Add Invalid Contact    | Submit with empty/malformed data            | Error validation shows              |

### 2.2 Upload Contact (CSV)
| TC-04 | Upload Valid CSV       | 1. Click `Upload Contact`<br>2. Select valid CSV<br>3. Submit | Contacts imported successfully |
| TC-05 | Upload Invalid CSV     | Upload corrupted/empty CSV                  | "Invalid file format" error     |

### 2.3 Individual/Group Sections
| TC-06 | View Individual Contacts | Navigate to `Individual Section`            | Lists all individual contacts    |
| TC-07 | View Group Contacts      | Navigate to `Group Section`                 | Lists all grouped contacts       |

### 2.4 Side Features
| TC-08 | Search Contacts          | Use search bar with name/number             | Correct contact appears          |
| TC-09 | Filter Contacts          | Apply filters (Group/Network)               | List updates dynamically         |
| TC-10 | Print Contacts           | Click `Print`                               | Generates printable report       |

## 3. Schedule Module

### 3.1 Projection Dashboard
| TC-11 | View Projections         | Check `Today`, `Tomorrow`, `Week`, `Monthly`, `All Pending` | Correct schedules displayed |

### 3.2 Schedule Section
| TC-12 | Schedule List            | Verify columns: `Name`, `No. of Contacts`, etc. | Data populated accurately |
| TC-13 | Pause/Delete Schedule    | Click `Pause` or `Delete`                     | Schedule updates status    |

### 3.3 Group Contact Schedule
| TC-14 | Group Schedule List      | Check columns: `Name`, `Mobile No.`, etc.     | Data matches group contacts |

### 3.4 Detail View
| TC-15 | Schedule Details         | Open `Detail View` of a schedule              | Shows all schedule metadata |

### 3.5 Side Features
| TC-16 | Search Schedules         | Use search bar for schedule name              | Correct schedule appears    |
| TC-17 | Filter Schedules         | Filter by `Frequency`/`Status`                | List updates accordingly    |

## 4. Transaction Module
| TC-18 | Pending Transactions     | Navigate to `Pending`                         | Lists pending transactions  |
| TC-19 | On-Demand History        | Check `On Demand History`                     | Shows past transactions     |
| TC-20 | Transaction Report       | Click `Print`                                 | Generates transaction log   |

## 5. Edge Cases
| TC-21 | Bulk Actions             | Pause/delete 10+ schedules at once            | Handles bulk operations     |
| TC-22 | Network Loss             | Disconnect during CSV upload                  | Graceful error recovery     |

## Test Notes
- **Priority Areas**: Schedule Module (High), Contact Upload (Medium)
- **Test Data Needed**: 
  - Sample CSV files (valid/invalid)
  - 50+ dummy contacts
  - Scheduled transactions with different frequencies