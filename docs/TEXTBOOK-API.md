> [Home](README.md) > Textbook API
---

# Textbook API

### **get_books_data(course_info)**

#### **Parameters**:
  - `courses_info`: List of dictionaries of class info | Example: `get_books_data([{'department_code': 'CS', 'course_name': 'CS0401', 'instructor': 'HOFFMAN', 'term': '2600'}]`

#### **Returns**:
Returns a list of dictionaries containing Author, ISBN, Edition, Title, and Citation

#### **Example**:

###### **Code**:
```python
get_books_data([{'department_code': 'CS', 'course_name': 'CS0401', 'instructor': 'HOFFMAN', 'term': '2600'}, {'department_code': 'CS', 'course_name': 'CS0445', 'instructor': 'GARRISON III', 'term': '2600'}])
```

###### **Sample Output**:
```python
  [
    {
      'author': 'Gaddis',
      'isbn': '9780133957051',
      'edition': '6',
      'citation': '<em>Starting Out W/Java:From.. W/Access</em> by Gaddis. Pearson Education, 6th Edition, 2015. (ISBN: 9780133957051).',
      'title': 'Starting Out W/Java:From... W/Access'
    },
    {
      'author': 'Carrano',
      'isbn': '9780133744057',
      'edition': '4',
      'citation': '<em>Data Struct.+Abstract.W/Java W/Access</em> by Carrano. Pearson Education, 4th Edition, 2014. (ISBN: 9780133744057).',
      'title': 'Data Struct.+Abstract.W/Java W/Access'
    }
  ]
```

### **get_department_url(department_code,term)**

#### **Parameters**:
  - `department_code`: Code for department | Example: `CS` or `LATIN`
  - `term` : ID for class term | Example `2600`
    - Default value is `2600` for Spring 2017

#### **Returns**:
Returns a department url corresponding to the format used by pitt.verbacompare.com

#### **Example**:

###### **Code**:
```python
textbook.get_department_url('CS', '2600')
```
###### **Sample Output**:
```python
http://pitt.verbacompare.com/compare/courses/?id=22457&term_id=2600
````
