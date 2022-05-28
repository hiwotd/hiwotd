from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class home(models.Model):
    pic=models.ImageField(upload_to='home_images')
    about=models.TextField()
    title=models.TextField()
    servicedes=models.TextField()
    def __str__(self):
       return self.about
class Video(models.Model):
    video=models.FileField(upload_to='videos/')
    summary=models.CharField( max_length=200)

class Author(models.Model):
    author=models.TextField()
    #imge = models.ImageField(upload_to='images_Author')
    def __str__(self):
        return self.author
class catagory(models.Model):
    cata=models.TextField()
    def __str__(self):
        return self.cata
class contact(models.Model):
    filel=models.FileField()
    name=models.TextField()
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()
    def __str__(self):
        return self.name 
    class Meta:  
        db_table = "contact"  
class news(models.Model):
    title=models.TextField()
    description=models.TextField()
    date=models.DateField()
    img = models.ImageField(upload_to='images_news')
    imges=models.ImageField(upload_to='images_Author',blank=True, null=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    #catagory=models.TextField()
    cata=models.ForeignKey(catagory, on_delete=models.CASCADE)
    search=models.TextField( )  
    quote=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title

class comment(models.Model):
    commenter=models.TextField()
    email=models.EmailField()
    comm=models.TextField()
    datecommented = models.DateTimeField(blank=True, null=True,auto_now=True)
    news=models.ForeignKey(news, on_delete=models.CASCADE)
    def __str__(self):
        return self.commenter

class notification(models.Model):
   title= models.TextField(blank=True, null=True)
   description=models.TextField(blank=True, null=True)
   #download=models.FileField(blank=True, null=True)
   img = models.ImageField(upload_to='images_notification', blank=True, null=True)
  
   def __str__(self):
       return self.title
class managment(models.Model):
    name=models.TextField(blank=True, null=True)
    author=models.TextField(blank=True, null=True)
    doc= models.FileField(blank=True, null=True)
    INTEGRATED='IN'
    QUALITY = 'QMS'
    acts = [
        (INTEGRATED, 'Integrated'),
        (QUALITY, 'Qms'),
    ]
    act = models.CharField(
        max_length=10,
        choices=acts,
        default=INTEGRATED,
    )

    def is_upperclass(self):
        return self.acts in {self.INTEGRATED, self.QUALITY}
class integrated(models.Model):
    name=models.TextField(blank=True, null=True)
    down= models.FileField(blank=True, null=True)
    MODULEONE = 'M1'
    MODULETWO= 'M2'
    MODULETHREE= 'M3'
    MODULEFOUR= 'M4'
    MODULEFIVE= 'M5'
    MODULESIX= 'M6'
    MODULESEVEN = 'M7'
    #NONIONIZING= 'NI'
    #INSPECTION = 'IN'
    #ENFORCEMENT= 'EN'
    services = [
        (MODULEONE, 'Moduleone'),
        (MODULETWO, 'Moduletwo'),
        (MODULETHREE, 'Modulethree'),
        (MODULEFOUR, 'Modulefour'),
        (MODULEFIVE, 'Modulefive'),
        (MODULESIX, 'Modulesix'),
        (MODULESEVEN, 'Moduleseven'),
        #(NONIONIZING, 'Non-ionizing'),
       # (INSPECTION, 'Inspection'),
        #(ENFORCEMENT, 'Enforcement'),
    ]
    serve = models.CharField(
       max_length=200,
       choices=services,
       default=MODULEONE,
    )

    def is_upperclass(self):
        return self.services in {self.MODULEONE, self.MODULETWO, self.MODULETHREE, 
        self.MODULEFOUR, self.MODULEFIVE, self.MODULESIX, self.MODULESEVEN}
        #, self.NON-IONIZING, self.INSPECTION, self.ENFORCEMENT}

class workingP(models.Model):
    name=models.TextField(blank=True, null=True)
    down= models.FileField(blank=True, null=True)
    DIRECTIVES= 'DIRECTIVE'
    GUIDLINES = 'GUIDLINE'
    LEGISLATIONS='LEGISLATION'
    OPERATIONALFORMATS= 'OPERATIONAL'
    POLICYDOCUMENTS='POLICY'
    REQUIREMENTS='REQUIREMENT'
    WORKINGPROCEDURE='WORKING'
    #INSPECTION = 'IN'
    #ENFORCEMENT= 'EN'
    services = [
        (DIRECTIVES, 'Directives'),
        (GUIDLINES, 'Guidlines'),
        (LEGISLATIONS, 'Legislation'),
        (OPERATIONALFORMATS, 'Operational'),
        (POLICYDOCUMENTS, 'Policy'),
        (REQUIREMENTS, 'Requirements'),
        (WORKINGPROCEDURE, 'Working'),
        #(NONIONIZING, 'Non-ionizing'),
       # (INSPECTION, 'Inspection'),
        #(ENFORCEMENT, 'Enforcement'),
    ]
    serve = models.CharField(
       max_length=200,
       choices=services,
       default=DIRECTIVES,
    )

    def is_upperclass(self):
        return self.services in {self.DIRECTIVES, self.GUIDLINES, self.LEGISLATIONS, 
        self.OPERATIONALFORMATS, self.POLICYDOCUMENTS, self.REQUIREMENTS, self.WORKINGPROCEDURE}
        #, self.NON-IONIZING, self.INSPECTION, self.ENFORCEMENT}
class researchL(models.Model):
    name=models.TextField(blank=True, null=True)
    down= models.FileField(blank=True, null=True)
    HIGHLIGHTSTYPESOFREASEARCHS= 'HIGHLIGHTSTYPESofREASEARCH'
    RESEARCHHYPOTHESISANDTESTING = 'RESEARCHHYPOTHESISandTESTING'
    FORMATINGRESEARCHOBJECTIVES='FORMATINGRESEARCHOBJECTIVE'
    MAKINGANEFFECTIVELETERACHREREVIEW= 'MAKINGanEFFECTIVELETERACHREREVIEW'
    TYPESOFRESEARCHDESIGNANDAPPLICATIONS='TYPESofRESEARCHDESIGNandAPPLICATIONS'
    TYPESOFDATA='TYPESofDATA'
    DATAPROCESSINGANDANALYSIS='DATAPROCESSINGandANALYSIS'
    STASTICALDATAANALYSISS='STASTICALDATAANALYSIS'
    RESEARCHWRITINGS ='RESEARCHWRITING'
    ETHICSINREASEARCH=' ETHICSinREASEARCH'
    RADIATIONPROTECTIONJOURNALS='RADIATIONPROTECTIONJOURNAL'
    IOPJOURNALS='IOPJOURNAL'
    ERPAJOURNALS ='ERPAJOURNAL'
    ERPAANDENVIRONMENTS='ERPAANDENVIRONMENT'
    ERPADOSIMETRYS='ERPADOSIMETRY'

    #INSPECTION = 'IN'
    #ENFORCEMENT= 'EN'
    services = [
        (HIGHLIGHTSTYPESOFREASEARCHS, 'HighlightsTypesofResearch'),
        (RESEARCHHYPOTHESISANDTESTING, 'ResearchHypothesisandTesting'),
        (FORMATINGRESEARCHOBJECTIVES, 'FormatingResearchObjectives'),
        (MAKINGANEFFECTIVELETERACHREREVIEW, 'MakinganEffectiveLeteracherReview'),
        (TYPESOFRESEARCHDESIGNANDAPPLICATIONS, 'TypesofResearchDesignandApplications'),
        (TYPESOFDATA, 'TypesofData'),
        (DATAPROCESSINGANDANALYSIS, 'DataProcessingandAnalysis'),
        (STASTICALDATAANALYSISS, 'StasticalDataAnalysis'),
        (RESEARCHWRITINGS, 'ResearchWriting'),
        (ETHICSINREASEARCH, 'EthicsinResearch'),
        (RADIATIONPROTECTIONJOURNALS, 'RadiationProtectionJournals'),
        (IOPJOURNALS, 'IOPJournals'),
        (ERPAJOURNALS, 'ERPAJournals'),
        (ERPAANDENVIRONMENTS, 'ERPAandEnvironment'),
        (ERPADOSIMETRYS, 'ERPADosimetry'),
        #(NONIONIZING, 'Non-ionizing'),
       # (INSPECTION, 'Inspection'),
        #(ENFORCEMENT, 'Enforcement'),
    ]
    serve = models.CharField(
       max_length=400,
       choices=services,
       default=HIGHLIGHTSTYPESOFREASEARCHS,
    )

    def is_upperclass(self):
        return self.services in {self.HIGHLIGHTSTYPESOFREASEARCHS, self.RESEARCHHYPOTHESISANDTESTING, self.FORMATINGRESEARCHOBJECTIVES, 
        self.MAKINGANEFFECTIVELETERACHREREVIEW, self.TYPESOFRESEARCHDESIGNANDAPPLICATIONS, self.TYPESOFDATA, self.DATAPROCESSINGANDANALYSIS,
        self.STASTICALDATAANALYSISSS, self.RESEARCHWRITINGS, self.ETHICSINREASEARCH, self.RADIATIONPROTECTIONJOURNALS, self.IOPJOURNALS,
        self.ERPAJOURNALS,self.ERPAANDENVIRONMENTS, self.ERPADOSIMETRYS}

class labratory(models.Model):
    name=models.TextField(blank=True, null=True)
    down= models.FileField(blank=True, null=True)
    ADDISPTTRAINING= 'ADDISptTRAINING'
    GAMMASPECTROMETERY = 'GAMMASpectrometry'
    LABRATORY='LAbratory'
    LECTURESANDEXERCISE= 'LECTURESandEXERCISE'
    TRAININGDOCUMENTSESTIMATIONOFUNCERTAINITY='TRAININGDOCUMENTESTIMATIONofINCERTAINITY'
    UNCERTAINITY='UNcertainity'
    UNCERTAINITYMEASUREMENT='UNCERTAINITYMeasurement'
    #INSPECTION = 'IN'
    #ENFORCEMENT= 'EN'
    services = [
        (ADDISPTTRAINING, 'Addispttraining'),
        (GAMMASPECTROMETERY, 'Gammaspectrometery'),
        (LABRATORY, 'Labratory'),
        (LECTURESANDEXERCISE, 'Lecturesandexercise'),
        (TRAININGDOCUMENTSESTIMATIONOFUNCERTAINITY, 'Trainingdocumentsestimationofuncertainity'),
        (UNCERTAINITY, 'Uncertainity'),
        (UNCERTAINITYMEASUREMENT, 'Uncertainitymeasurement'),
    ]
    serve = models.CharField(
       max_length=400,
       choices=services,
       default=ADDISPTTRAINING,
    )

    def is_upperclass(self):
        return self.services in {self.ADDISPTTRAINING, self.GAMMASPECTROMETERY, self.LABRATORY, 
        self.LECTURESANDEXERCISE, self.TRAININGDOCUMENTSESTIMATIONOFUNCERTAINITY, self.UNCERTAINITY, self.UNCERTAINITYMEASUREMENT}


class NIRD(models.Model):
    name=models.TextField(blank=True, null=True)
    down= models.FileField(blank=True, null=True)
    GENERALONNIR= 'GENERALonNIR'
    ITECEMFONTELECOMINDIA = 'ITECEMFonTELECOMINDIA'
    LASERRELATEDDOCUMENTS='LASERRELATEDDOCUMENT'
    MICROWAVERELATEDDOCUMENTS= 'MICROWAVERELATEDDOCUMENT'
    MRIRELATEDDOCUMENTS='MRIRELATEDDOCUMENT'
    RFRELATEDDOCUMENTS='RFRELATEDDOCUMENT'
    UVRELATEDDOCUMENTS='UVRELATEDDOCUMENT'
    #INSPECTION = 'IN'
    #ENFORCEMENT= 'EN'
    services = [
        (GENERALONNIR, 'Generalonnir'),
        (ITECEMFONTELECOMINDIA, 'Itecemfontelecomindia'),
        (LASERRELATEDDOCUMENTS, 'Laserrelateddocuments'),
        (MICROWAVERELATEDDOCUMENTS, 'Microwaverelateddocuments'),
        (MRIRELATEDDOCUMENTS, 'Mrirelateddocuments'),
        (RFRELATEDDOCUMENTS, 'Rfrelateddocuments'),
        (UVRELATEDDOCUMENTS, 'Uvrelateddocuments'),
    ]
    serve = models.CharField(
       max_length=400,
       choices=services,
       default=GENERALONNIR,
    )

    def is_upperclass(self):
        return self.services in {self.GENERALONNIR, self.ITECEMFONTELECOMINDIA, self.LASERRELATEDDOCUMENTS, 
        self.MICROWAVERELATEDDOCUMENTS, self.MRIRELATEDDOCUMENTS, self.RFRELATEDDOCUMENTS, self.UVRELATEDDOCUMENTS}

class Safeguards(models.Model):
    name=models.TextField(blank=True, null=True)
    down= models.FileField(blank=True, null=True)
    CTBTOOSITRAININGMATERIALS= 'CTBTOOSITRAININGMATERIAL'
    SMALLQUANTITYPROTOCOLS= 'SMALLQUANTITYPROTOCOL'
    OSI='THEOSI'
    ARROUNDTHEGLOBEANDCLOCK= 'ARROUNDtheGLOBEandCLOCK'
    #INSPECTION = 'IN'
    #ENFORCEMENT= 'EN'
    services = [
        (CTBTOOSITRAININGMATERIALS, 'CTBTOOSITrainingMaterial'),
        (SMALLQUANTITYPROTOCOLS, 'SmallQuantityProtocols'),
        (OSI, ' Osi'),
        (ARROUNDTHEGLOBEANDCLOCK, 'ArroundtheGlobeandClock'),
        #(NONIONIZING, 'Non-ionizing'),
       # (INSPECTION, 'Inspection'),
        #(ENFORCEMENT, 'Enforcement'),
    ]
    serve = models.CharField(
       max_length=400,
       choices=services,
       default=CTBTOOSITRAININGMATERIALS,
    )

    def is_upperclass(self):
        return self.services in {self.CTBTOOSITRAININGMATERIALS, self.SMALLQUANTITYPROTOCOL, 
        self.OSI, self.ARROUNDTHEGLOBEANDCLOCK}

class safetyP(models.Model):
    name=models.TextField(blank=True, null=True)
    down= models.FileField(blank=True, null=True)
    EDUCATIONTRAININGS= 'EDUCATIONTRAINING'
    EMERGENCYPREPARDENESSRESPONSES= '  EMERGENCYPREPARDENESSRESPONS'
    PUBLICENVIRONMENTALRADIOLOGICALPROTECTIONS=' PUBLICENVIRONMENTALRADIOLOGICALPROTECTIONS'
    RADIOLOGICALPROTECTIONFORINDUSTRIESANDRESEARCH= 'RADIOLOGICALPROTECTIONforINDUSTRIESandRESEARCH'
    RADIATIONPROTECTIONINMEDICALEXPOSORE='RADIATIONPROTECTIONinMEDICALEXPOSORE'
    RADIATIONPROTECTIONINOCCUPATIONALEXPOSORE ='RADIATIONPROTECTIONinOCCUPATIONALEXPOSORE'
    REGULATORYINFRUSTRACTURES ='   REGULATORYINFRUSTRACTURE'
    TRANSPORTSAFETYS='TRANSPORTSAFETYS'
    #INSPECTION = 'IN'
    #ENFORCEMENT= 'EN'
    services = [
        (EDUCATIONTRAININGS , 'EducationTraining'),
        (EMERGENCYPREPARDENESSRESPONSES, 'EmergencyPrepardnessResponse'),
        (PUBLICENVIRONMENTALRADIOLOGICALPROTECTIONS,' PublicEnvironmentalRadiologicalProtection'),
        (RADIOLOGICALPROTECTIONFORINDUSTRIESANDRESEARCH, 'RadiologicalProtectionforIndustriesandResearch'),
        (RADIATIONPROTECTIONINMEDICALEXPOSORE,'RadiationProtectioninMedicalExposore'),
        (RADIATIONPROTECTIONINOCCUPATIONALEXPOSORE ,'RadiationProtectionin OccupationalExposore'),
        (REGULATORYINFRUSTRACTURES ,'RegulatoryInfrastructure'),
        (TRANSPORTSAFETYS,'TransportSafety'),

        #(NONIONIZING, 'Non-ionizing'),
       # (INSPECTION, 'Inspection'),
        #(ENFORCEMENT, 'Enforcement'),
    ]
    serve = models.CharField(
       max_length=400,
       choices=services,
       default=EDUCATIONTRAININGS,
    )

    def is_upperclass(self):
        return self.services in {self.EDUCATIONTRAININGS, self.EMERGENCYPREPARDENESSRESPONSES, self.PUBLICENVIRONMENTALRADIOLOGICALPROTECTIONS, 
        self.RADIOLOGICALPROTECTIONFORINDUSTRIESANDRESEARCH, self.RADIATIONPROTECTIONINMEDICALEXPOSORE,
         self.RADIATIONPROTECTIONINOCCUPATIONALEXPOSORE, self.REGULATORYINFRUSTRACTURES, self.TRANSPORTSAFETYS}

class Security(models.Model):
    name=models.TextField(blank=True, null=True)
    down= models.FileField(blank=True, null=True)
    SECURITYOFRADIOACTIVEMATERIALS= 'SECURITYOFRADIOACTIVEMATERIAL'
    COMPUTERSECURITYS= 'COMPUTERSECURITY'
    TRANSPORTSECURITYS=' TRANSPORTSECURITY'
    PHYSICALPROTECTIONS= ' PHYSICALPROTECTION'

    #INSPECTION = 'IN'
    #ENFORCEMENT= 'EN'
    services = [
        (SECURITYOFRADIOACTIVEMATERIALS,'SecurityofRadioactiveMaterials'),
        (COMPUTERSECURITYS, 'ComputerSecurity'),
        (TRANSPORTSECURITYS,'TransportSecurity'),
        (PHYSICALPROTECTIONS,'PhysicalProtection'),

        #(NONIONIZING, 'Non-ionizing'),
       # (INSPECTION, 'Inspection'),
        #(ENFORCEMENT, 'Enforcement'),
    ]
    serve = models.CharField(
       max_length=400,
       choices=services,
       default=SECURITYOFRADIOACTIVEMATERIALS,
    )

    def is_upperclass(self):
        return self.services in {self.SECURITYOFRADIOACTIVEMATERIALS, self.COMPUTERSECURITYS,
         self.TRANSPORTSECURITYS, self.PHYSICALPROTECTIONS}


class usefullD(models.Model):
    name=models.TextField(blank=True, null=True)
    down= models.FileField(blank=True, null=True)
    NATIONALPRESENTATIONS= 'NATIONALPRESENTATION'
    ERPACOLLECTIVES= 'ERPACOLLECTIVE'
    SOFTWARES='SOFTWARE'

    #INSPECTION = 'IN'
    #ENFORCEMENT= 'EN'
    services = [
        (NATIONALPRESENTATIONS,'NationalPresentations'),
        (ERPACOLLECTIVES, 'ERPACollectives'),
        (SOFTWARES,'Software'),
        

        #(NONIONIZING, 'Non-ionizing'),
       # (INSPECTION, 'Inspection'),
        #(ENFORCEMENT, 'Enforcement'),
    ]
    serve = models.CharField(
       max_length=400,
       choices=services,
       default=NATIONALPRESENTATIONS,
    )

    def is_upperclass(self):
        return self.services in {self.NATIONALPRESENTATION, self.ERPACOLLECTIVE, self.SOFTWARE}

class events(models.Model):
    name=models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='event_images', blank=True, null=True)
    #catago=models.TextField(blank=True, null=True)
    ANNUALCONFERENCE='AC'
    MOU = 'MO'
    WORKSHOP = 'WO'
    VISIT = 'VI'
    OTHER= 'OT'
    event = [
        (ANNUALCONFERENCE, 'Annual Conference'),
        (MOU, 'MOU'),
        (WORKSHOP, 'Workshops'),
        (VISIT, 'Scientific Vist'),
        (OTHER, 'Others'),
    ]
    even = models.CharField(
        max_length=2,
        choices=event,
        default=ANNUALCONFERENCE,
    )

    def is_upperclass(self):
        return self.event in {self.ANNUALCONFERENCE, self.MOU}


class vacancy(models.Model):
   title= models.TextField(blank=True, null=True)
   description=models.TextField(blank=True, null=True)
   typev=models.TextField(blank=True, null=True)
   #doc=models.FileField(blank=True, null=True)
   def __str__(self):
       return self.title
class apply(models.Model):
   fullName= models.TextField(blank=True, null=True)
   dateofbirth=models.DateField(blank=True, null=True)
   nationality=models.TextField(blank=True, null=True)
   education=models.TextField(blank=True, null=True)
   jobPosition=models.TextField(blank=True, null=True)
   workExperiance=models.IntegerField(blank=True, null=True)
   grade=models.FloatField(blank=True, null=True)
   gender=models.TextField(blank=True, null=True)
   phone=models.TextField(blank=True, null=True)
   email=models.EmailField(blank=True, null=True)
   name=models.CharField(max_length =100, blank=True, null=True)
   attachment=models.FileField(upload_to='documents/', blank=True, null=True)
   def __str__(self):
       return self.jobPosition
   class Meta:
      db_table = "attachment"


class User(models.Model):
    username=models.TextField(blank=True, null=True)
    password= models.TextField(blank=True, null=True)

class Tacitk(models.Model):
    tacitvideo=models.FileField(upload_to='tacitvideos/')
    summaryv=models.CharField( max_length=400)
    RESEARCHTACITS= 'RESEARCHTACIT'
    LABRATORYTACITS= 'LABRATORYTACIT'
    INSPECTIONTACITS='INSPECTIONTACIT'
    ENFORCEMENTTACITS= 'ENFORCEMENTTACIT'
    services = [
        (RESEARCHTACITS, 'ResearchTacit'),
        (LABRATORYTACITS, 'LabratoryTacit'),
        (INSPECTIONTACITS, ' InspectionTacit'),
        (ENFORCEMENTTACITS, 'EnforcementTacit'),
    ]
    serve = models.CharField(
       max_length=600,
       choices=services,
       default=RESEARCHTACITS,
    )

    def is_upperclass(self):
        return self.services in {self.RESEARCHTACITS, self.LABRATORYTACITS, 
        self.INSPECTIONTACITS, self.ENFORCEMENTTACITS}