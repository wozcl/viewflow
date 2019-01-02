from viewflow import flow, frontend
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from .models import OficinaPartesProcess, VacacionesProcess


@frontend.register
class OficinaPartesFlow(Flow):
    process_class = OficinaPartesProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=['remitente','institucion','region','ciudad','jefe','mejoramigo']
        ).Permission(
            auto_create=True
        ).Next(this.tarea1)
    )

    tarea1 = (
        flow.View(
            UpdateProcessView,
            fields=['remitente', 'institucion', 'region', 'ciudad']
        ).Permission(
            auto_create=True
        ).Next(this.approve)
    )

    tarea2 = (
        flow.View(
            UpdateProcessView,
            fields=['remitente', 'institucion']
        ).Permission(
            auto_create=True
        ).Next(this.send)
    )

    tarea3 = (
        flow.View(
            UpdateProcessView,
            fields=['remitente']
        ).Permission(
            auto_create=True
        ).Next(this.end)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=['approved']
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.tarea2)
        .Else(this.tarea3)
    )

    send = (
        flow.Handler(
            this.send_oficina_partes_request
        ).Next(this.end)
    )

    end = flow.End()

    def send_oficina_partes_request(self, activation):
        print(activation.process.remitente)

@frontend.register
class VacacionesFlow(Flow):
    process_class = VacacionesProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=['nombre','apellido','fecha_nacimiento','document']
        ).Permission(
            auto_create=True
        ).Next(this.end)
    )

    end = flow.End()

    def send_vacaciones_request(self, activation):
        print(activation.process.nombre)


