import { Button, DestructiveButton } from '@sheleg-design/workbench';

export const DeleteWorkspace = () => (
  <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
    <DestructiveButton
      confirmLabel="Delete — confirm"
      onClick={() => console.log('workspace deleted')}
    >
      Delete workspace
    </DestructiveButton>
    <Button variant="ghost" onClick={() => console.log('cancelled')}>
      Cancel
    </Button>
  </div>
);

/**
 * How it looks after the first click. `armed` is internal state, so this
 * specimen pins the class the component adds and gives the label the same
 * text in both states — it behaves exactly as it looks.
 */
export const ArmedAfterFirstClick = () => (
  <DestructiveButton
    className="wb-btn--armed"
    confirmLabel="Revoke key — confirm"
    onClick={() => console.log('key revoked')}
  >
    Revoke key — confirm
  </DestructiveButton>
);

export const DisabledWithoutPermission = () => (
  <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
    <DestructiveButton disabled>Drop table orders.v2</DestructiveButton>
    <Button variant="ghost" size="sm" onClick={() => console.log('request')}>
      Request owner access
    </Button>
  </div>
);
