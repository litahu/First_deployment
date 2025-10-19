# 🎫 Implementación y supervisión de un flujo de trabajo de aprendizaje automático en AWS

## 💡 1. Descripción del Proyecto

Este proyecto implementa un flujo de trabajo completo de Machine Learning para clasificación de imágenes en AWS, específicamente diseñado para distinguir entre bicicletas y motocicletas. La solución utiliza servicios serverless de AWS para crear una arquitectura escalable y de bajo costo que incluye:

- **Extracción y preparación** de datos del dataset CIFAR-100
- **Entrenamiento** de un modelo de clasificación de imágenes usando Amazon SageMaker
- **Despliegue** del modelo como endpoint en tiempo real
- **Orquestación** del flujo de trabajo usando AWS Step Functions
- **Procesamiento serverless** con AWS Lambda
- **Monitoreo** del modelo con SageMaker Model Monitor

El proyecto simula un caso de uso real para "Scones Unlimited", una empresa de delivery que necesita clasificar vehículos automáticamente para optimizar rutas de entrega.

## ☁ 2. Herramientas y Servicios Utilizados

### Archivos Principales
- **starter.ipynb**: Notebook que contiene todo el flujo de ETL, entrenamiento y despliegue
- **lambda1.py**: Función Lambda que descarga imágenes de S3 y las codifica en base64
- **lambda2.py**: Función Lambda que invoca el endpoint de SageMaker para predicciones
- **lambda3.py**: Función Lambda que filtra predicciones con confianza > 93%
- **step-function-definition.json**: Configuración del Step Function que orquesta el flujo

### AWS Services
- **Amazon SageMaker**: Entrenamiento y despliegue del modelo
- **AWS Lambda**: Funciones serverless para procesamiento
- **AWS Step Functions**: Orquestación del workflow
- **Amazon S3**: Almacenamiento de datos y modelos
- **IAM**: Gestión de permisos y roles de seguridad
- **CloudWatch**: Monitoreo y logging

<p align="center">
    <kbd> <img width="900" alt="jkhjk" src= "https://github.com/litahu/First_deployment/blob/main/assest/cloudAWS_1.PNG" > </kbd> <br>
    Image — Interacciones con la nube de Amazon Web Services
</p>

<p align="center">
    <kbd> <img width="900" alt="jkhjk" src= "https://github.com/litahu/First_deployment/blob/main/assest/cloudAWS_2.PNG" > </kbd> <br>
    Image — AWS Lambda
</p>

<p align="center">
    <kbd> <img width="900" alt="jkhjk" src= "https://github.com/litahu/First_deployment/blob/main/assest/cloudAWS_3.PNG" > </kbd> <br>
    Image — Test de AWS Lambda
</p>

## 🏆 3. Experiencia con Microservicios de Amazon

**La curva de aprendizaje fue real** 😅
- Comprendí que generar los IAM es propio de cada microservicio, ya que cada uno formula politicas muy personalizadas(¡Requiere paciencia, pero evita problemas después!)  
- Con Amazon States Language (ASL) para Step Functions tuve que una alta curva de aprendizaje, pero el editor visual me ayudo mucho a comprenderlo

**Lo que más me costó:**
- Entender cómo pasar datos entre Lambdas en Step Functions
- Depurar cuando algo falla en medio del workflow
- Recordar que cada servicio tiene sus "propios eventos"

**Lo que más me gustó:**
- Ver el workflow completo funcionando en Step Functions es súper satisfactorio
- La documentación de AWS es extensa (a veces demasiado, pero está todo ahí)
- Poder probar cada Lambda individualmente antes de integrarlas


## 📊 4. Resultados

### Métricas del Modelo
- **Accuracy en Validación**: 82%
- **Precisión para Bicicletas**: 85%
- **Precisión para Motocicletas**: 79%
- **Umbral de Confianza**: 93%

![pagina](https://github.com/litahu/First_deployment/blob/main/assest/cloudAWS_1.1.gif)

### Performance del Sistema
- **Tiempo de Inferencia**: < 2 segundos end-to-end
- **Disponibilidad**: 99.95% (gracias a la infraestructura AWS)
- **Escalabilidad**: Hasta 1000+ invocaciones concurrentes

### Monitoreo Implementado
- Captura de datos de entrada/salida del endpoint
- Métricas de confianza en tiempo real
- Alertas para inferencias de baja confianza
- Dashboard de CloudWatch para monitoreo continuo

<p align="center">
    <kbd> <img width="800" alt="jkhjk" src= "https://github.com/litahu/First_deployment/blob/main/assest/cloudAWS_8.PNG" > </kbd> <br>
    Image — Monitoreando el flujo de las predicciones superiores al umbral 0.93
</p>


## 💖 6. Agradecimiento

Este proyecto fue posible gracias a:

- **Amazon Web Services y Udacity** por proporcionarme una plataforma robusta con documentación exhaustiva para implementar un modelo de machine learning de forma muy vivida.
- **Mi familia** por facilitarme su apoyo incondicional(¡Me inspiran cada día!)
- **Los instructores y compañeros** por el feedback valioso durante el desarrollo(¡Me ayudaron a acercarme más al entorno cloud. Gracias infinitas!)



