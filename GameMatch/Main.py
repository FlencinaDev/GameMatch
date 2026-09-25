# ==================================================
#             Control de consultas
# ==================================================

continuar = "Si"

while continuar == "Si":

    # ==================================================
    # DATOS DEL JUGADOR
    # ==================================================

    edad = int(input("⌛ Ingrese su edad: "))
    experiencia_jugando = int(input("⭐ Ingrese su experiencia jugando (1 - 10): "))
    tiempo_disponible = int(input("⌚ Ingrese su tiempo disponible en minutos: "))
    estado_animo = input("👦 Ingrese su estado de ánimo (Tranquilo/Intenso): ")

    presupuesto = float(input("💸 Ingrese su presupuesto: "))
    cantidad_jugadores = int(input("👥 Cantidad de jugadores (1 - 10): "))
    genero_preferido = input("🔹 Ingrese el género preferido (Shooter/Terror/Supervivencia/Simulación/Casual/Acción): ")
    dificultad_deseada = int(input("🔻 Ingrese la dificultad deseada (1 - 10): "))
    plataforma = input("🖥️ Ingrese su plataforma (PC/Consola/Mobile): ")

    le_gusta_competir = input("🎮 ¿Sos competitivo? (Si/No): ")
    le_gusta_socializar = input("💬 ¿Te gusta socializar? (Si/No): ")


    # ==================================================
    #              CONVERTIR RESPUESTAS
    # ==================================================

    if le_gusta_competir == "Si":
        quiere_competir = True
    else:
        quiere_competir = False

    if le_gusta_socializar == "Si":
        quiere_socializar = True
    else:
        quiere_socializar = False


    # ==================================================
    # CALCULOS
    # ==================================================

    if quiere_competir:
        bonus_competitivo = 2
    else:
        bonus_competitivo = 0

    puntaje_exigencia = experiencia_jugando + dificultad_deseada + bonus_competitivo

    if tiempo_disponible < 30:
        categoria_tiempo = "Muy poco"
    elif tiempo_disponible < 60:
        categoria_tiempo = "Poco"
    elif tiempo_disponible <= 120:
        categoria_tiempo = "Moderado"
    else:
        categoria_tiempo = "Mucho"

    if experiencia_jugando <= 3:
        categoria_experiencia = "Principiante"
    elif experiencia_jugando <= 5:
        categoria_experiencia = "Intermedio"
    elif experiencia_jugando <= 7:
        categoria_experiencia = "Avanzado"
    else:
        categoria_experiencia = "Experto"

    if puntaje_exigencia <= 7:
        categoria_exigencia = "Baja"
    elif puntaje_exigencia <= 13:
        categoria_exigencia = "Media"
    elif puntaje_exigencia <= 18:
        categoria_exigencia = "Alta"
    else:
        categoria_exigencia = "Muy alta"

    if categoria_experiencia == "Avanzado" or categoria_experiencia == "Experto":
        es_experto_o_avanzado = True
    else:
        es_experto_o_avanzado = False

    if categoria_exigencia == "Alta" or categoria_exigencia == "Muy alta":
        es_exigencia_alta = True
    else:
        es_exigencia_alta = False


    # ==================================================
    # MOTOR DE REGLAS
    # ==================================================

    score = 0

    recomendacion_1 = ""
    recomendacion_2 = ""
    recomendacion_3 = ""

    nueva_recomendacion = ""


    # -------------------- R1 --------------------------

    # Partida rápida

    if tiempo_disponible <= 60 and quiere_competir and dificultad_deseada >= 6:
        if genero_preferido == "Shooter":
            nueva_recomendacion = "CS2, Valorant o Fortnite"
        elif genero_preferido == "Acción":
            nueva_recomendacion = "Fortnite"
        else:
            nueva_recomendacion = ""

        score = score + 10

        if nueva_recomendacion != "":
            if recomendacion_1 == "":
                recomendacion_1 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
                recomendacion_2 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
                recomendacion_3 = nueva_recomendacion


    # -------------------- R2 --------------------------

    # Sesión larga

    if tiempo_disponible > 120 and not quiere_competir and dificultad_deseada <= 6:
        if genero_preferido == "Supervivencia":
            nueva_recomendacion = "Minecraft o Terraria"
        elif genero_preferido == "Simulación":
            nueva_recomendacion = "Stardew Valley"
        elif genero_preferido == "Casual":
            nueva_recomendacion = "Fall Guys"
        else:
            nueva_recomendacion = ""

        score = score + 10

        if nueva_recomendacion != "":
            if recomendacion_1 == "":
                recomendacion_1 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
                recomendacion_2 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
                recomendacion_3 = nueva_recomendacion


    # -------------------- R3 --------------------------

    # Perfil competitivo

    if quiere_competir and experiencia_jugando >= 6 and dificultad_deseada >= 7:
        if genero_preferido == "Shooter":
            nueva_recomendacion = "CS2, Valorant o Fortnite"
        elif genero_preferido == "Acción":
            nueva_recomendacion = "Fortnite"
        else:
            nueva_recomendacion = ""

        score = score + 15

        if nueva_recomendacion != "":
            if recomendacion_1 == "":
                recomendacion_1 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
                recomendacion_2 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
                recomendacion_3 = nueva_recomendacion


    # -------------------- R4 --------------------------

    # Jugador social

    if cantidad_jugadores >= 2 and quiere_socializar and tiempo_disponible >= 45:
        if genero_preferido == "Supervivencia":
            nueva_recomendacion = "Minecraft"
        elif genero_preferido == "Terror":
            nueva_recomendacion = "Lethal Company o Phasmophobia"
        else:
            nueva_recomendacion = ""

        score = score + 15

        if nueva_recomendacion != "":
            if recomendacion_1 == "":
                recomendacion_1 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
                recomendacion_2 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
                recomendacion_3 = nueva_recomendacion


    # -------------------- R5 --------------------------

    # Buscador de terror

    if genero_preferido == "Terror" and estado_animo == "Intenso" and dificultad_deseada >= 5:
        nueva_recomendacion = "Phasmophobia, Outlast o Dead by Daylight"

        score = score + 15

        if recomendacion_1 == "":
            recomendacion_1 = nueva_recomendacion
        elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
            recomendacion_2 = nueva_recomendacion
        elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
            recomendacion_3 = nueva_recomendacion


    # -------------------- R6 --------------------------

    # Quiero relajarme

    if estado_animo == "Tranquilo" and not quiere_competir and dificultad_deseada <= 5:
        if genero_preferido == "Simulación":
            nueva_recomendacion = "Stardew Valley"
        elif genero_preferido == "Supervivencia":
            nueva_recomendacion = "Minecraft"
        else:
            nueva_recomendacion = ""

        score = score + 10

        if nueva_recomendacion != "":
            if recomendacion_1 == "":
                recomendacion_1 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
                recomendacion_2 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
                recomendacion_3 = nueva_recomendacion


    # -------------------- R7 --------------------------

    # Presupuesto cero

    if presupuesto == 0 and plataforma == "PC":
        if genero_preferido == "Shooter":
            nueva_recomendacion = "CS2, Valorant o Fortnite"
        elif genero_preferido == "Acción":
            nueva_recomendacion = "Fortnite"
        else:
            nueva_recomendacion = ""

        score = score + 10

        if nueva_recomendacion != "":
            if recomendacion_1 == "":
                recomendacion_1 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
                recomendacion_2 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
                recomendacion_3 = nueva_recomendacion


    # -------------------- R8 --------------------------

    # Jugador experimentado

    if experiencia_jugando >= 8 and dificultad_deseada >= 8 and quiere_competir:
        if genero_preferido == "Shooter":
            nueva_recomendacion = "CS2, Valorant o Fortnite"
        elif genero_preferido == "Acción":
            nueva_recomendacion = "Fortnite"
        else:
            nueva_recomendacion = ""

        score = score + 15

        if nueva_recomendacion != "":
            if recomendacion_1 == "":
                recomendacion_1 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
                recomendacion_2 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
                recomendacion_3 = nueva_recomendacion


    # -------------------- R9 --------------------------

    # Jugador casual

    if experiencia_jugando <= 4 and dificultad_deseada <= 5 and not quiere_competir:
        if genero_preferido == "Supervivencia":
            nueva_recomendacion = "Minecraft"
        elif genero_preferido == "Simulación":
            nueva_recomendacion = "Stardew Valley"
        elif genero_preferido == "Casual":
            nueva_recomendacion = "Fall Guys"
        else:
            nueva_recomendacion = ""

        score = score + 10

        if nueva_recomendacion != "":
            if recomendacion_1 == "":
                recomendacion_1 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
                recomendacion_2 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
                recomendacion_3 = nueva_recomendacion


    # -------------------- R10 -------------------------

    # Experiencia intensa

    if estado_animo == "Intenso" and dificultad_deseada >= 7 and experiencia_jugando >= 6 and tiempo_disponible >= 30:
        if genero_preferido == "Shooter":
            nueva_recomendacion = "Fortnite"
        elif genero_preferido == "Terror":
            nueva_recomendacion = "Dead by Daylight"
        elif genero_preferido == "Acción":
            nueva_recomendacion = "Fortnite"
        else:
            nueva_recomendacion = ""

        score = score + 20

        if nueva_recomendacion != "":
            if recomendacion_1 == "":
                recomendacion_1 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
                recomendacion_2 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
                recomendacion_3 = nueva_recomendacion


    # -------------------- R11 -------------------------

    # Amigos + terror

    if cantidad_jugadores >= 2 and quiere_socializar and genero_preferido == "Terror" and estado_animo == "Intenso":
        nueva_recomendacion = "Phasmophobia, Lethal Company o Dead by Daylight"

        score = score + 20

        if recomendacion_1 == "":
            recomendacion_1 = nueva_recomendacion
        elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
            recomendacion_2 = nueva_recomendacion
        elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
            recomendacion_3 = nueva_recomendacion


    # -------------------- R12 -------------------------

    # Perfil competitivo ideal

    if es_experto_o_avanzado and es_exigencia_alta and quiere_competir and tiempo_disponible >= 30:
        if genero_preferido == "Shooter":
            nueva_recomendacion = "CS2, Valorant o Fortnite"
        elif genero_preferido == "Acción":
            nueva_recomendacion = "Fortnite"
        else:
            nueva_recomendacion = ""

        score = score + 20

        if nueva_recomendacion != "":
            if recomendacion_1 == "":
                recomendacion_1 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 == "":
                recomendacion_2 = nueva_recomendacion
            elif recomendacion_1 != nueva_recomendacion and recomendacion_2 != nueva_recomendacion and recomendacion_3 == "":
                recomendacion_3 = nueva_recomendacion


    # ==================================================
    #               RESULTADO FINAL
    # ==================================================

    if score >= 90:
        resultado_general = "Compatibilidad excelente"
    elif score >= 70:
        resultado_general = "Compatibilidad muy alta"
    elif score >= 50:
        resultado_general = "Compatibilidad alta"
    elif score >= 30:
        resultado_general = "Compatibilidad moderada"
    else:
        resultado_general = "Compatibilidad baja"


    # ==================================================
    #              MOSTRAR RESULTADOS
    # ==================================================

    print("╔══════════════════════════════════════════╗")
    print("║                                          ║")
    print("║             🎮 GAMEMATCH 🎮             ║")
    print("║                                          ║")
    print("╠══════════════════════════════════════════╣")
    print("║            RECOMENDACIONES               ║")
    print("╚══════════════════════════════════════════╝")

    print("╔══════════════════════════════════════════╗")
    print("║                RESULTADO                 ║")
    print("╠══════════════════════════════════════════╣")

    if recomendacion_1 != "":
        print("🎮", recomendacion_1)

    if recomendacion_2 != "":
        print("🎮", recomendacion_2)

    if recomendacion_3 != "":
        print("🎮", recomendacion_3)

    if recomendacion_1 == "" and recomendacion_2 == "" and recomendacion_3 == "":
        print("❌ No se encontraron recomendaciones específicas para este perfil.")


    print("╠══════════════════════════════════════════╣")
    print("║ 🎯 Score final:", score)
    print("║ 📊 Resultado:", resultado_general)
    print("╚══════════════════════════════════════════╝")

    # ==================================================
    #              NUEVA CONSULTA
    # ==================================================

    print("╔══════════════════════════════════════════════════════╗")
    continuar = input("🔄 ¿Querés realizar otra consulta? (Si/No): ")
    print("╚══════════════════════════════════════════════════════╝")


#controlar las consultas
