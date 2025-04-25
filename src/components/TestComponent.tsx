import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
export default function TestComponent() {
  return (
    <Card className="p-4">
      <CardHeader>
        <CardTitle>Prueba de Componentes</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <Input placeholder="Prueba de input" />
        <Button>Prueba de botón</Button>
      </CardContent>
    </Card>
  );
}