#Design
####COMP4 Coursework Feedback and Marking
There are **12 marks** available for this section.

|Name|Candidate No.|Centre No.|Draft Mark|Final Mark|
|-|-|-|:-:|:-:|
|Tommy THAM | |22151|**5**|**8** |

##Overall Comments

+ Design feasible but some errors/inconsistencies
+ Most criteria considered in depth, but some more basic

##Layout

|**Strengths**||
|-|-|
|Framework used| |
|**Weaknesses**||
|Blank pages| |

##Overall System Design

###Short description of the main parts of the system

|**Strengths**||
|-|-|
|Useful descriptions of UI flow and actions|Useful descriptions of UI flow and actions |
|**Weaknesses**||
|Be clear about core elements of system not just UI| |

###System flowcharts showing an overview of the complete system

|**Strengths**||
|-|-|
||Flowcharts show several processes largely clear |
|**Weaknesses**||
|Unclear about adding items to orders, and adding items to menu|Some errors in flowcharts |
|Booking date/time clash? | |

##User Interface Designs

|**Strengths**||
|-|-|
|Clear sequence, with some good design features|UI designs with some clear reasons |
|**Weaknesses**||
|Multiple users - own logins? Anyone change the password?| |
|How can an order be checked? | |
|Consider easier method for entering items to order| |
|Check logic - clicking Delete again to end deleting is not user friendly| |

##Hardware Specification

|**Strengths**||
|-|-|
|Brief comment|Gives specification detail of client hardware |
|**Weaknesses**||
|Many more details needed| |

##Program Structure

###Top-down design structure charts

|**Strengths**||
|-|-|
||Structure charts show processes and some data flows |
|**Weaknesses**||
|Show decision symbols (diamonds) and loops| |
|Adding details - surely all added in one process? | |

###Algorithms in pseudo-code for each data transformation process

|**Strengths**||
|-|-|
||Basic algorithms included |
|**Weaknesses**||
|Calculate price algorithm incorrect| |

###Object Diagrams

|**Strengths**||
|-|-|
|| Main objects identified and relationships outlined |
||Shows aggregations of objects|
|**Weaknesses**||
|Menu is an object| |
|Contains errors - e.g. number of customers for a booking; tables making orders| |

###Class definitions

|**Strengths**||
|-|-|
|Basics with some elements identified|Main classes identified and attributes/methods listed |
|**Weaknesses**||
|Inconsistent with UI designs|Not all clearly defined (e.g. Customer) |Some inconsistencies e.g Customer|
|Set methods for each attribute| |

##Prototyping

###Consideration of impact on design and development

|**Strengths**||
|-|-|
|Some basic ideas considered|Basic ideas considered |
|**Weaknesses**||
|Make sure ideas are clearly explained| |
|Linking to database?| |
|Finding current customers' orders rather than previous ones for table? | |

##Definition of Data Requirements

###Identification of all data input items

|**Strengths**||
|-|-|
|Some inputs identified|Identifies range of inputs |
|**Weaknesses**||
|Several inputs missing| |

###Identification of all data output items

|**Strengths**||
|-|-|
|Good to identify different outputs|Identifies range of outputs and where required in system |
|**Weaknesses**||
|Check all outputs included - e.g. number of items ordered on Order window| |
|All stored items should be output to database | |

###Explanation of how data output items are generated

|**Strengths**||
|-|-|
|Clear basic descriptions|Clear basic descriptions of generation of output |
|**Weaknesses**||
|| |

###Data Dictionary

|**Strengths**||
|-|-|
|Data dictionary included|Elements of data dictionary included |
|**Weaknesses**||
|Length and range seem muddled|Table not displayed correctly so missing content |

###Identification of appropriate storage media

|**Strengths**||
|-|-|
|Basic statement|Basic statement with consideration of backup medium |
|**Weaknesses**||
|Needs more details| |

##Database Design

###ER Diagram

|**Strengths**||
|-|-|
||ERD included |
|**Weaknesses**||
|Booking has become Reservation|Lacking explanation of why customer and order is 1-1 (customer details not stored, so each 'sitting' is a new customer |
|No relationship between Customer and Menu | |
|Why has Customer many Orders? | |
|Inconsistent with entity descriptions | |

###Entity Descriptions and UNF to 3NF

|**Strengths**||
|-|-|
|Appropriate descriptions and UNF to 3NF| |
|**Weaknesses**||
|| |

###SQL Queries

|**Strengths**||
|-|-|
||Basic SQL queries |
|**Weaknesses**||
|SQL rather than python code| |
|Limited examples| |
|Selecting a current table's order needs including| |

##Security and Integrity of the System and Data

###Security and Integrity of Data

|**Strengths**||
|-|-|
|Basic comment|Sound comments |
|**Weaknesses**||
|What personal data stored?| |
|Needs much more detail | |

###System Security

|**Strengths**||
|-|-|
|Basic comment|Basic comment |
|**Weaknesses**||
|Needs much more detail| |

##Validation

|**Strengths**||
|-|-|
|Some validation identified|Some appropriate validation included |
|**Weaknesses**||
|Be precise, not vague about criteria|Non-standard terms used (e.g. float check, number check) |
|Check correct validation identified e.g. where lookup check is better than range check | |

##Testing

###Outline Plan

|**Strengths**||
|-|-|
|Range of test types| |
|**Weaknesses**||
|Integration testing?| |

###Detailed Plan

|**Strengths**||
|-|-|
|Some suitable strategies for basic tests|Suitable strategies for basic tests with some test data|
|**Weaknesses**||
|Rows in table not clear|Multiple test items given for tests - erroneous, and normal in same test row (separate tests?) |
|Be consistent - isn't time entered automatically? | |
|Further tests needed | |