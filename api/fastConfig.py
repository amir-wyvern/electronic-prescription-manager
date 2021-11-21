
class Swagger:

    __description = """
### *Electronic Prescription Manager*
*epm is a interface api that allows the registration and management of electronic prescriptions
It also has other facilities such as better clinic management and patient medical records*

### *Features*
- *Register ,Edit & Remove electronic prescription*
- *Clinic management*
- ✨ *Patient medical record*✨

> *This version is still under development* 
> *and some of its features may not work*

"""
    
    attrs = {
        'title' : 'EPM Backend',
        'description' : __description,
        'version' : '0.0.1',
        'docs_url' : '/docs',  # swagger UI
        'redoc_url' : '/'     # Redoc UI
    }