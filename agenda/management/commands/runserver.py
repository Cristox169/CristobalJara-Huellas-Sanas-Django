"""Run the development server and print direct links to the Huellas Sanas pages."""

from django.contrib.staticfiles.management.commands.runserver import (
    Command as DjangoRunserverCommand,
)


class Command(DjangoRunserverCommand):
    """Keep Django's server behavior and make the local URLs easy to find."""

    def on_bind(self, server_port):
        super().on_bind(server_port)

        if self._raw_ipv6:
            host = f"[{self.addr}]"
        elif self.addr in {"", "0", "0.0.0.0"}:
            host = "127.0.0.1"
        else:
            host = self.addr

        base_url = f"{self.protocol}://{host}:{server_port}"
        links = (
            ("Página Huellas Sanas", f"{base_url}/"),
            ("Panel de administración", f"{base_url}/admin/"),
        )

        self.stdout.write("\nEnlaces rápidos (copia o Ctrl+clic):")
        for label, url in links:
            self.stdout.write(f"  {label}: {url}")
            terminal_link = f"\033]8;;{url}\033\\Abrir {label}\033]8;;\033\\"
            self.stdout.write(f"    {terminal_link}")
        self.stdout.flush()
